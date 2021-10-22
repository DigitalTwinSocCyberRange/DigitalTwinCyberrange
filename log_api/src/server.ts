import express from 'express';
import fs from 'fs';
import readLastLines from 'read-last-lines';

/**
 * Express server for sending log changes as Server Sent Events
 */
export class ExpressServer {
  private logfiles = ['/logs/plc1.log', '/logs/plc2.log', '/logs/plc3.log'];

  /**
   * constructor
   */
  constructor() { }

  /**
   * Starts the express server to listen for connections
   */
  public start(): void {
    console.log('starting...');
    const app = express();
    app.get('/events', async (req: any, res: any) => {
      console.log('Got /events');
      res.set({
        'Cache-Control': 'no-cache',
        'Content-Type': 'text/event-stream',
        'Connection': 'keep-alive',
      });
      res.flushHeaders();

      // Tell the client to retry every 10 seconds if connectivity is lost
      res.write('retry: 10000\n\n');

      this.watchFiles(this.logfiles, (lastline: string) => {
        console.log(lastline);
        this.writeLog(res, lastline);
      });
    });

    const index = fs.readFileSync('./index.html', 'utf8');
    app.get('/', (req: any, res: any) => res.send(index));

    app.listen(3000);
    console.log('Listening on port 3000');
  }

  /**
   * Reads the last line of a file
   * @param filename The filename of the file
   * @returns Returns the last line as a Promise
   */
  private async readLastLine(filename: string): Promise<string> {
    return await readLastLines.read(filename, 1);
  }

  /**
   * Sends a log to the event stream
   * @param res Response of the get request
   * @param log The log to write to the event stream
   */
  private writeLog(res: any, log: string) {
    res.write(`data: ${log}\n\n`);
  }

  /**
   * Watches a file for changes
   * @param filename The path to the file to watch
   * @param lastline Callback which is triggered when the file
   * changed, returning the last line of the watched file
   */
  private watchFile(
      filename: string,
      lastline: (lastline: string) => void): void {
    fs.watch(filename, async (event: any, filename: any) => {
      console.log(`${filename} file changed`);
      lastline(await this.readLastLine(filename));
    });
  }

  /**
   * Watches multiple files for changes
   * @param filenames Array of file paths to watch
   * @param lastlines Callback which is triggered when a file
   * changed, returning the last line of the watched file
   */
  private watchFiles(
      filenames: string[],
      lastlines: (lastline: string) => void) {
    filenames.forEach((filename: string) => {
      this.watchFile(filename, (lastline) => {
        lastlines(lastline);
      });
    });
  }
}

const server = new ExpressServer();
server.start();
