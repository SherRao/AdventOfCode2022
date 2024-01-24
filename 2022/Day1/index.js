const fs = require('fs');

const main = async () => {
    const data = await fs.readFileSync('./input.txt', 'utf8');
    const lines = data.split("\n");
    const sums = [];
    let tempSum = 0;

    for(const line of lines) {
        if(line == "") {
            sums.push(tempSum);
            tempSum = 0;

        } else
            tempSum += parseInt(line);
    }

    console.log("Result:", Math.max(...sums));
};

main();
