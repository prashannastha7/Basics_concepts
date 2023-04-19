
import  Console from 'console';
import http from 'http';

const port = process.env.port || 3000; // use for using port number of own

const server = http.createServer((req, res) =>{
    //console.log(req);
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html')
    res.end('<h1> This is just practise</h1> <p>Keep moving on</p>')
})

server.listen(port, ()=>{
    console.log(`Server is listening on port ${port}`);
});