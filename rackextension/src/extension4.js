"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var child_process_1 = require("child_process");
var readline = require("readline");
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.question('Enter something: ', function (userInput) {
    console.log('User input:', userInput);
    var pythonScriptPath = '/Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py';
    var pythonProcess = (0, child_process_1.spawn)('python3', [pythonScriptPath]);
    pythonProcess.stdin.write(userInput);
    pythonProcess.stdin.end();
    pythonProcess.stdout.on('data', function (data) {
        console.log('Python script output:');
        console.log(data.toString());
    });
    pythonProcess.stderr.on('data', function (data) {
        console.error("Error from Python script: ".concat(data.toString()));
    });
    pythonProcess.on('close', function (code) {
        console.log("Python script exited with code ".concat(code));
        rl.close(); // Close the readline interface when done
    });
});
// Listen for close event on readline interface
rl.on('close', function () {
    console.log('Readline closed.');
});
