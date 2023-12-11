import * as vscode from 'vscode';
import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('What is your name? ', (answer: string) => {
  console.log(`Hello, ${answer}!`);
  rl.close();
});

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