
import  Console from 'console';
import http from 'http';
import fs from 'fs'

const port = process.env.port || 3000; // use for using port number of own

const server = http.createServer((req, res) =>{
    res.statusCode=200;
    res.setHeader('Content-Type', 'text/html')
    console.log(req.url);

    if (req.url == '/'){
        res.statusCode = 200;
        res.end('<h1> Home page</h1> <p>Keeping moving</p>')
    }
    else if(req.url == '/hello'){
        res.statusCode = 200;
        const data = fs.readFileSync('index.html')
        res.end(data.toString())
    }
    else if(req.url == '/about'){
        res.statusCode = 200;
        res.end('<h1> About</h1> <p>this is about page</p>')
    }
    else{
        res.statusCode= 404;
        res.end("<h1> Not Found </h1><p> This page is not found in the server</p>")
    }
})

server.listen(port, ()=>{
    console.log(`Server is listening on port ${port}`);
});