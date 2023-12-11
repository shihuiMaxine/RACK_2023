import { spawn } from 'child_process';
import * as readline from 'readline';
import * as vscode from 'vscode';

async function searchSnippets() {
  const selectedText = '';  // You would have some logic to get selected text, not provided here

  const searchQuery = await vscode.window.showInputBox({
    placeHolder: "Search query",
    prompt: "Search my snippets on Codever",
    value: selectedText
  });

  if (searchQuery === '') {
    console.log(searchQuery);
    vscode.window.showErrorMessage('A search query is mandatory to execute this action');
  } else {
    // Execute the action based on the searchQuery (not provided in the snippet)
    console.log('Executing action with search query:', searchQuery);
  }
}

// Call the function to initiate the search
searchSnippets();


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
