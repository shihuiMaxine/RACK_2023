import * as vscode from 'vscode';
// import * as cp from 'child_process';
import { spawn } from 'child_process';
async function searchSnippets(searchQuery: string): Promise<void> {
  if (searchQuery === '') {
    console.log(searchQuery);
    vscode.window.showErrorMessage('A search query is mandatory to execute this action');
  } else if (searchQuery !== undefined) {
    // Replace with the actual path to "rack1.py"
    const filePath = 'rack1.py';

    // Run "rack1.py" and pass the searchQuery as input
    const rack1Process = spawn('python', [filePath, searchQuery]);

    let output = '';

    // Handle standard output
    rack1Process.stdout.on('data', (data) => {
      output += data.toString();
    });

    // Handle standard error
    rack1Process.stderr.on('data', (data) => {
      console.error('rack1.py stderr:', data.toString());
    });

    // Handle process exit
    rack1Process.on('close', (code) => {
      console.log('rack1.py process exited with code', code);

      // Display the output using vscode.env.openExternal
      vscode.env.openExternal(vscode.Uri.parse('data:text/plain;charset=utf-8,' + encodeURIComponent(output)));
    });
  }
}

// async function main() {
//   const searchQuery = await vscode.window.showInputBox({
//     placeHolder: 'Search query',
//     prompt: 'Search my snippets on Codever',
//     value: selectedText,
//   });

//   await runRack1WithInput(searchQuery);
// }

// // Call the main function to start the search
// main();
