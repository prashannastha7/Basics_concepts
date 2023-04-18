const path = require('path')

const a = path.basename('A:\\espanol.txt')
const a2 = path.dirname('A:\\espanol.txt')
const a3 = path.extname(__filename)
console.log(a)
console.log(a3)

//FS module 

const fs = require('fs')

const x = fs.readFileSync('file.txt')
console.log(x.toString())
console.log("Finished reading file")

const y = fs.writeFileSync('file.txt', "you are learning.")
console.log(y)