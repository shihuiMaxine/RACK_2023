// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import * as cp from "child_process";
import * as readline from 'readline';
// import * as readline from 'readline';
// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "rackextension" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('rackextension.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		const message='Hello World from rackextension!'
		vscode.window.showInformationMessage(message);
	});

	context.subscriptions.push(disposable);
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
		  } else if (searchQuery !== undefined) {
			console.log(searchQuery);
			console.log("working");

			// // Replace with the actual path to "rack1.py"
			const filePath = "rack1.py";
			const pythonScriptPath = '/Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py';
			const inputArgument = searchQuery;
			console.log("python3 /Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py -q " + String(inputArgument));

			
			cp.exec("python3 /Users/gaoshihui/Desktop/whltest10/rackextension/src/rack1.py -q " + String(inputArgument), (err, stdout, stderr) => {
				console.log('stdout: ' + stdout);
				console.log('stderr: ' + stderr);
				if (err) {
					console.log('error: ' + err);
				}			
			});
			
			
			
		  }
		}
	  
	  
	  // Call the function to initiate the search
	  searchSnippets();
	  context.subscriptions.push(disposable);
	  // This method is called when your extension is deactivated
	//   export function deactivate() {}
	  
}


export function deactivate() {}

	  
	//     if (searchQuery === '') {
	//       console.log(searchQuery);
	//       vscode.window.showErrorMessage('A search query is mandatory to execute this action');
	//     } else {
	//   	// const searchUrl = `https://www.codever.land/search?q=${searchQuery}&sd=my-snippets`;
	//     	// vscode.env.openExternal(Uri.parse(searchUrl));
	  
	//       // Execute the action based on the searchQuery (not provided in the snippet)
	//       console.log('Executing action with search query:', searchQuery);
	//     }
	//   }
	  
	  // async function searchSnippets(searchQuery: string): Promise<void> {



			// // // Run "rack1.py" and pass the searchQuery as input
			// const rack1Process = spawn('python3', [filePath, searchQuery]);
		
			// let output = '';
		
			// // Handle standard output
			// rack1Process.stdout.on('data', (data) => {
			//   output += data.toString();
			// });
		
			// // Handle standard error
			// rack1Process.stderr.on('data', (data) => {
			//   console.error('rack1.py stderr:', data.toString());
			// });
		
			// // Handle process exit
			// rack1Process.on('close', (code) => {
			//   console.log('rack1.py process exited with code', code);
		
			  // Display the output using vscode.env.openExternal
			//   vscode.env.openExternal(vscode.Uri.parse('data:text/plain;charset=utf-8,' + encodeURIComponent(output)));
			// });
