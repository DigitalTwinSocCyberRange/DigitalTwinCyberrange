import express from "express";
import fs from 'fs';
import readLastLines from "read-last-lines";
// run().catch(err => console.log(err));

export class ExpressServer {
  app = express();
  logfiles = ['./index.html', './server.js'];

  constructor() {

  }

  public start(): void {
    console.log('starting...')
    this.app.get('/events', async (req: any, res: any) => {
      console.log('Got /events');
      res.set({
        'Cache-Control': 'no-cache',
        'Content-Type': 'text/event-stream',
        'Connection': 'keep-alive'
      });
      res.flushHeaders();

      // Tell the client to retry every 10 seconds if connectivity is lost
      res.write('retry: 10000\n\n');
      let count = 0;

      this.watchFiles(this.logfiles, (lastline: string) => {
        console.log(lastline);
        this.writeLog(res, lastline);
      });
    });

    const index = fs.readFileSync('./index.html', 'utf8');
    this.app.get('/', (req: any, res: any) => res.send(index));

    this.app.listen(3000);
    console.log('Listening on port 3000');
  }

  private async readLastLine(filename: string): Promise<string> {
    return await readLastLines.read(filename, 1);
  }

  private writeLog(res: any, log: string) {
    res.write(`data: ${log}\n\n`);
  }

  private watchFile(filename: string, lastline: (lastline: string) => void) {
    fs.watch(filename, async (event: any, filename: any) => {
      console.log(`${filename} file changed`);
      lastline(await this.readLastLine(filename));
    });
  }

  private watchFiles(filenames: string[], lastlines: (lastline: string) => void) {
    filenames.forEach((filename: string) => {
      this.watchFile(filename, (lastline) => {
        lastlines(lastline);
      });
    });
  }
}

let server = new ExpressServer();
server.start();