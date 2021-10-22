"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.ExpressServer = void 0;
const express_1 = __importDefault(require("express"));
const fs_1 = __importDefault(require("fs"));
const read_last_lines_1 = __importDefault(require("read-last-lines"));
// run().catch(err => console.log(err));
class ExpressServer {
    constructor() {
        this.app = (0, express_1.default)();
        this.logfiles = ['/logs/plc1.log', '/logs/plc2.log', '/logs/plc3.log'];
    }
    start() {
        console.log('starting...');
        this.app.get('/events', (req, res) => __awaiter(this, void 0, void 0, function* () {
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
            this.watchFiles(this.logfiles, (lastline) => {
                console.log(lastline);
                this.writeLog(res, lastline);
            });
        }));
        const index = fs_1.default.readFileSync('./index.html', 'utf8');
        this.app.get('/', (req, res) => res.send(index));
        this.app.listen(3000);
        console.log('Listening on port 3000');
    }
    readLastLine(filename) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield read_last_lines_1.default.read(filename, 1);
        });
    }
    writeLog(res, log) {
        res.write(`data: ${log}\n\n`);
    }
    watchFile(filename, lastline) {
        fs_1.default.watch(filename, (event, filename) => __awaiter(this, void 0, void 0, function* () {
            console.log(`${filename} file changed`);
            lastline(yield this.readLastLine(filename));
        }));
    }
    watchFiles(filenames, lastlines) {
        filenames.forEach((filename) => {
            this.watchFile(filename, (lastline) => {
                lastlines(lastline);
            });
        });
    }
}
exports.ExpressServer = ExpressServer;
let server = new ExpressServer();
server.start();
