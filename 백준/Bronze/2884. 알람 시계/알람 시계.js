const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' '); 
    
    let hour = parseInt(input[0]);
    let minute = parseInt(input[1]);
    
    if(minute - 45 < 0){
        minute = minute + 60 - 45;
        hour -= 1;
        
        if(hour === -1){
            hour = 23;
        }
    } else {
        minute -= 45;
    }
    console.log(`${hour} ${minute}`); 
  })
  .on('close', function () {
    process.exit();
  });