import * as readline from 'readline';
import { spawn } from 'child_process';
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('What is your name? ', (answer: string) => {
  console.log(`Hello, ${answer}!`);
  rl.close();
});
