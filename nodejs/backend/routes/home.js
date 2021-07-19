const express=require('express');
const router=express.Router();
var mysql      = require('mysql');
// 비밀번호는 별도의 파일로 분리해서 버전관리에 포함시키지 않아야 합니다. 
var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : 'A1b2c3d4e5!',
  database : 'developer'
});
var app=express();
connection.connect();
  

connection.query('select * from t_CMN_COTN_MST', function(error, results){
        if ( error ){
            response.status(400).send('Error in database operation');
        } else {
            response.send(results);
        }
});
  
connection.end();