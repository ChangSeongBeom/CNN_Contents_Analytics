var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var mysql      = require('mysql');

var indexRouter = require('./routes/index');
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'A1b2c3d4e5!',
  database : 'developer'
});

// var usersRouter = require('./routes/users');
// var loginRouter = require('./routes/login');
// const movieRouter = require('./routes/movie');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
// app.use('/users', usersRouter);
//app.use('/movies', movieRouter);


app.get('/users', (req, res) => {
  connection.query('SELECT * from t_cmn_yolo_log', (error, rows) => {
    if (error) throw error;
    console.log('User info is: ', rows);
    res.send(rows);
  });
});

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});









app.get('/', (req, res) => {
  res.send('Root');
});



app.listen(app.get('port'), () => {
  console.log('Express server listening on port ' + app.get('port'));
});




module.exports = app;
