import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

export const getLines = (importMetaUrl: string): string[] => {
  const __dirname = fileURLToPath(new URL('.', importMetaUrl));
  const inputPath = join(__dirname, 'input.txt');
  const examplePath = join(__dirname, 'example.txt');

  let activePath: string;

  if (existsSync(inputPath)) {
    activePath = inputPath;
  } else if (existsSync(examplePath)) {
    console.warn('input.txt not found, falling back to example.txt');
    activePath = examplePath;
  } else {
    throw new Error('No input.txt or example.txt found in this directory.');
  }

  return readFileSync(activePath, 'utf-8').trim().split('\n');
};
