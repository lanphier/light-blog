var gulp = require('gulp');
var sass = require('gulp-sass');
var globbing = require('gulp-css-globbing');
var cssimport = require("gulp-cssimport");
var autoprefixer = require('gulp-autoprefixer');

var notifier = require('node-notifier');

function notifyError(){
	notifier.notify({
	  'title': 'error',
	  'message': 'gulp error'
	});
}

gulp.task('sass', function () {
  return gulp.src('./stylesheets/application.scss')
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
    .pipe(gulp.dest('./css'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./stylesheets/**/*.scss', ['sass']);
});