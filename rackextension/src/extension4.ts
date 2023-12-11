import { spawn } from 'child_process';
import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter something: ', (userInput) => {
  console.log('User input:', userInput);

  const pythonScriptPath = 'rack1.py';
  const pythonProcess = spawn('python3', [pythonScriptPath]);

  pythonProcess.stdin.write(userInput);
  pythonProcess.stdin.end();

  pythonProcess.stdout.on('data', (data) => {
    console.log('Python script output:');
    console.log(data.toString());
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Error from Python script: ${data.toString()}`);
  });

  pythonProcess.on('close', (code) => {
    console.log(`Python script exited with code ${code}`);
    rl.close();  // Close the readline interface when done
  });
});

// Listen for close event on readline interface
rl.on('close', () => {
  console.log('Readline closed.');
});
