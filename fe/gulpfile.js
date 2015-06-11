var gulp = require('gulp');
var sass = require('gulp-sass');
var globbing = require('gulp-css-globbing');
var cssimport = require("gulp-cssimport");
var autoprefixer = require('gulp-autoprefixer');
var uglify = require('gulp-uglify');
var minifyCss = require('gulp-minify-css');
var rev = require('gulp-rev');
var revReplace = require('gulp-rev-replace');
var replace = require('gulp-replace');
var runSequence = require('run-sequence');
var del = require('del');

var notifier = require('node-notifier');

var static_path = 'build/static';
var templates_path = 'build/app/templates';

function notifyError(){
	notifier.notify({
	  'title': 'error',
	  'message': 'gulp error'
	});
}

function config(deploy_type){
  if(deploy_type == 'test'){
    static_path += '2';
  }else if(deploy_type == 'prod'){

  }
}

// 清楚临时构建文件夹 build/ static/css static/js
gulp.task('clean', function(cb){
    del(['build','static/css','static/js'], cb);
})

// 编译 scss 文件 为 css
gulp.task('sass', function () {
  return gulp.src('./stylesheets/page/*.scss')
  	.pipe(cssimport({
  		extensions: ['.css']
  	}))
  	.pipe(globbing({
  		extensions: ['.scss']
  	}))
    .pipe(sass().on('error', notifyError))
    .pipe(autoprefixer({
        browsers: ['last 2 versions','IE 8'],
        cascade: true
    }))
    .pipe(gulp.dest('static/css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('stylesheets/**/*.scss', ['sass']);
});

// 对css 文件进行压缩处理
gulp.task('css',['sass'], function(){
  return gulp.src(['static/css/**/*.css'],{base : 'static'})
    .pipe(minifyCss({compatibility: 'ie8'}))
    .pipe(gulp.dest('build/'));
});

// 对 js 文件进行压缩处理
gulp.task('js', function(){
  return gulp.src(['static/js/**/*.js'],{base : 'static'})
    .pipe(uglify())
    .pipe(gulp.dest('build/'));
});

// 在 js、css文件名上添加hash字符串
gulp.task('hash', function(){
  return gulp.src(['build/**/*.js','build/**/*.css'])
    .pipe(rev())
    .pipe(gulp.dest('build'))
    .pipe(rev.manifest())
    .pipe(gulp.dest('build'));
});

// 改变html模板中对静态资源的引用路径
gulp.task('replace', function(){
  var manifest = gulp.src("build/rev-manifest.json");
  return gulp.src(['templates/**/*.html'])
    .pipe(revReplace({manifest: manifest}))
    .pipe(replace(/href=\"\/static/g,'href="/static'))
    .pipe(replace(/src=\"\/static/g,'src="/static'))
    .pipe(gulp.dest('build/templates'));
});

gulp.task('copy:bower', function(){
  return gulp.src(['static/bower/**/*'],{base: 'static'})
    .pipe(gulp.dest(static_path));
});

gulp.task('copy:static', function(){
  return gulp.src(['build/css/**/*','build/js/**/*'],{base: 'build'})
    .pipe(gulp.dest(static_path));
});

gulp.task('copy:templates', function(){
  return gulp.src(['build/templates/**/*'],{base: 'build'})
    .pipe(gulp.dest(templates_path));
});
// 拷贝处理完的静态资源、模板至指定目录
gulp.task('copy', ['copy:bower','copy:static','copy:templates']);

// 开发时启用
gulp.task('dev', function(){
  gulp.start(['sass','sass:watch']);
});

// 测试服务器部署使用
gulp.task('deploy:test', function(callback){
  config('test');
  runSequence('clean',['css','js'],'hash','replace','copy',callback);
});
// 正式服务器部署使用
gulp.task('deploy:prod', function(){
  config('prof');
  runSequence('clean',['css','js'],'hash','replace','copy',callback);
});

