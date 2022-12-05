const fs = require('fs');

const main = async () => {
    const possibilities = {"A": "X", "B": "Y", "C": "Z"};
    const data = await fs.readFileSync('./input.txt', 'utf8');
    const lines = data.split("\n");

    let score = 0;
    for(const line of lines) {
        if(line == undefined || line == "")
            continue;

        // Give points depending on choice
        const [a, b] = line.split(" ");
        switch(b) {
            case "X":
                score += 1;
                break;

            case "Y":
                score += 2;
                break;

            case "Z":
                score += 3;
                break;
        }

        // Draw
        if(possibilities[a] === b)
            score += 3;

        // Win
        else if((a == "A" && b == "Y") || (a == "B" && b == "Z") || (a == "C" && b == "X") )
            score += 6;
    }

    console.log("Result:", score);
};

main();
