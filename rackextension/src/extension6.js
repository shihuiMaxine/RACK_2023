// import * as vscode from 'vscode';
var vscode = require("vscode");
function activate() {
  const disposable = vscode.commands.registerCommand('extension.showInputBox', () => {
    vscode.window.showInputBox({
      placeHolder: 'Enter something',
      prompt: 'Please enter some text'
    }).then(value => {
      vscode.window.showInformationMessage('You entered: ' + value);
    });
  });

  context.subscriptions.push(disposable);
}

export function deactivate() {}
