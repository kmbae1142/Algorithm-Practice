const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const N = parseInt(input[0]);

for (let i = 1; i <= N; i++) {
    if (input[i].includes('S')) {
        console.log(input[i]);
        break;
    }
}