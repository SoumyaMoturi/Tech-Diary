# Node.js Interview Questions — Detailed Answers

---

## BEGINNER LEVEL

### 1. What is Node.js?

**Answer:** Node.js is a **JavaScript runtime built on Chrome's V8 engine** that lets you run JavaScript outside the browser — typically on a server. Before Node, JS could only run in a browser; Node gave it a runtime with access to the file system, networking, and OS-level APIs.

**Key characteristics:**
- **Event-driven, non-blocking I/O model**: instead of spawning a new thread per request (like traditional multi-threaded servers), Node uses a single main thread with an event loop that delegates I/O work (file reads, DB calls, network requests) to the system and continues processing other requests while waiting. When the I/O completes, a callback is queued back onto the main thread.
- **Single-threaded** (for JS execution) but can still achieve high concurrency because it's rarely *blocked* — it's mostly waiting on I/O, not computing.
- **npm ecosystem**: the largest package registry in the world, which is a major reason for Node's popularity — huge reuse of community libraries.

**Use cases:** REST/GraphQL APIs, real-time apps (chat, live notifications via WebSockets), microservices, streaming data pipelines, CLI tools, server-side rendering for frontend frameworks (Next.js, etc.).

**Where Node is a poor fit:** CPU-heavy workloads (image/video processing, heavy computation) since that blocks the single JS thread — for those, you'd offload to worker threads, a separate service, or a language better suited for parallel computation.

---

### 2. How does the event loop work in Node.js?

**Answer:** The event loop is the mechanism that allows Node to perform non-blocking I/O despite JavaScript being single-threaded. It continuously checks: *"is the call stack empty? If so, what's next in the queues?"*

**The phases, in order, each loop iteration ("tick"):**
1. **Timers** — runs callbacks scheduled by `setTimeout`/`setInterval` whose time has elapsed.
2. **Pending callbacks** — executes I/O callbacks deferred from the previous cycle (some system-level callbacks).
3. **Idle/prepare** — internal, not used by application code.
4. **Poll** — retrieves new I/O events (file reads, network responses) and executes their callbacks; this is where the loop spends most of its time if there's nothing else to do.
5. **Check** — runs `setImmediate()` callbacks.
6. **Close callbacks** — e.g., `socket.on('close', ...)`.

**Between every phase and after every single callback**, Node drains two special queues first:
- `process.nextTick()` queue (highest priority, Node-specific).
- The Promise **microtask** queue (`.then`, `async/await` continuations).

**Why it matters practically:** it's how a single Node process can handle thousands of concurrent connections — while one request is waiting on a database query (I/O), the event loop is free to process other incoming requests. It only becomes a bottleneck when you run **synchronous, CPU-bound code** on the main thread (e.g., a big `for` loop, synchronous JSON parsing of huge payloads, `bcrypt.hashSync`), because that blocks the loop and every other in-flight request has to wait.

---

### 3. What is the difference between `setImmediate` and `process.nextTick`?

**Answer:**
- **`process.nextTick(callback)`**: schedules the callback to run **immediately after the current operation completes**, before the event loop continues to any phase — it has its own queue that is fully drained (including any nextTicks added during draining) before microtasks or moving to the next phase. It's Node-specific (doesn't exist in browsers).
- **`setImmediate(callback)`**: schedules the callback to run in the **check phase** of the event loop, i.e., after the current poll phase completes. It effectively means "run this on the next iteration of the event loop, after I/O events for this cycle are handled."

**When to use which:**
- Use `process.nextTick` sparingly, for things that truly need to happen before I/O continues (e.g., emitting an error event right after object construction, before any other code runs) — **but be careful:** recursive/heavy use of `nextTick` can **starve the event loop** (I/O never gets a chance to run) because Node keeps draining the nextTick queue completely before moving on.
- Use `setImmediate` when you want to defer work until after the current I/O cycle, without the starvation risk — it's generally the safer choice for "run this soon, but don't block I/O."

**Ordering example:**
```js
setImmediate(() => console.log('immediate'));
process.nextTick(() => console.log('nextTick'));
Promise.resolve().then(() => console.log('promise'));
console.log('sync');
// Output: sync, nextTick, promise, immediate
// (sync code first, then nextTick queue, then microtask/Promise queue, then check phase for setImmediate)
```

---

### 4. Explain the difference between `readFileSync` and `readFile` in Node.js.

**Answer:**
- **`fs.readFileSync(path)`**: **blocking/synchronous**. Execution halts on this line until the entire file is read into memory; the result is returned directly. No other code (including other requests, if this is a server) runs while this is happening.
- **`fs.readFile(path, callback)`**: **non-blocking/asynchronous**. The read is delegated to Node's internal thread pool (via libuv); execution continues immediately to the next line, and the callback fires later when the read completes.

```js
// Synchronous — blocks the event loop
const data = fs.readFileSync('file.txt', 'utf-8');
console.log(data);

// Asynchronous — non-blocking
fs.readFile('file.txt', 'utf-8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// Modern promise-based version (fs/promises)
const data = await fs.promises.readFile('file.txt', 'utf-8');
```

**When to use `Sync` versions:** Generally **only** at startup/config-loading time (e.g., reading a config file before the server starts accepting requests), where blocking briefly is harmless because nothing else depends on the event loop yet. **Never** use sync file operations inside a request handler in a production server — it blocks every other in-flight request for the duration of the disk read.

---

### 5. What are streams in Node.js?

**Answer:** Streams let you process data **incrementally, in chunks**, rather than loading an entire resource into memory at once. This is critical for large files/payloads (video, large CSV exports, large API responses) where loading everything into memory would be slow or could crash the process.

**Four types:**
- **Readable**: a source you can read data *from* (e.g., `fs.createReadStream`, an incoming HTTP request body).
- **Writable**: a destination you can write data *to* (e.g., `fs.createWriteStream`, an HTTP response).
- **Duplex**: both readable and writable, independently (e.g., a TCP socket).
- **Transform**: a duplex stream that **modifies** data as it passes through (e.g., a gzip compressor, a CSV parser).

**Example — piping (the idiomatic way to connect streams):**
```js
const fs = require('fs');
const zlib = require('zlib');

fs.createReadStream('large-file.txt')
  .pipe(zlib.createGzip())          // Transform stream
  .pipe(fs.createWriteStream('large-file.txt.gz'));
```
`pipe()` automatically handles **backpressure** — if the destination is slower than the source, it pauses the source until the destination catches up, preventing memory buildup.

---

### 6. What is npm? How is it different from yarn?

**Answer:** **npm** (Node Package Manager) is the default package manager bundled with Node.js — it installs, manages, and publishes JS packages, and maintains `package.json` (declared dependencies) and `package-lock.json` (exact resolved dependency tree for reproducible installs).

**Yarn** is an alternative package manager (originally by Facebook) created to address early npm pain points: it was faster (parallel installs), had a lockfile (`yarn.lock`) before npm did, and offered deterministic installs earlier. Modern npm (v7+) has closed most of this gap — both now support lockfiles, workspaces (monorepos), and comparable performance.

**Practical differences today:** mostly command syntax (`yarn add` vs `npm install`), some differences in monorepo/workspace ergonomics, and Yarn Berry (v2+) introduced **Plug'n'Play** (no `node_modules` folder, resolves deps differently) which is a bigger architectural difference — but many teams still use "Yarn Classic" (v1) which behaves similarly to npm. In an interview, it's fine to say: "functionally very similar today; the choice is often just team/project convention."

---

### 7. Explain middleware in Express.js.

**Answer:** Middleware in Express is a function with the signature `(req, res, next)` that sits in the request-response pipeline. Each middleware can:
- Inspect/modify the `req`/`res` objects.
- End the request-response cycle (e.g., send a response and stop).
- Call `next()` to pass control to the next middleware in the chain.

If `next()` is never called (and no response is sent), the request **hangs forever**.

**Built-in middleware example:**
```js
app.use(express.json()); // parses JSON request bodies into req.body
app.use(express.static('public')); // serves static files
```

**Custom middleware example:**
```js
function requestLogger(req, res, next) {
  console.log(`${req.method} ${req.url} at ${new Date().toISOString()}`);
  next(); // must call this or the request stalls
}
app.use(requestLogger);

function authMiddleware(req, res, next) {
  const token = req.headers.authorization;
  if (!token) return res.status(401).json({ error: 'Unauthorized' }); // short-circuits, no next()
  req.user = verifyToken(token);
  next();
}
app.use('/orders', authMiddleware, ordersRouter); // scoped to a specific route
```
Middleware order matters — they execute in the order they're registered, so auth middleware must come before the routes it's protecting.

---

### 8. What is a callback function in Node.js?

**Answer:** A callback is a function passed as an argument to another function, to be invoked later — typically once an asynchronous operation completes. This is the original pattern Node used (before Promises/async-await became standard) to handle non-blocking I/O.

```js
fs.readFile('data.txt', 'utf-8', (err, data) => {
  if (err) {
    console.error('Failed to read file:', err);
    return;
  }
  console.log(data);
});
console.log('This logs BEFORE the file content, because readFile is non-blocking');
```

**How it avoids blocking:** the call to `readFile` returns immediately — Node doesn't wait for the disk read. The main thread continues executing subsequent code (the `console.log` after it). Only once the file system operation completes (handled by libuv's thread pool) does Node's event loop pick up the callback and execute it.

**Downside interviewers expect you to know:** deeply nested callbacks lead to "callback hell" (pyramid of doom), which Promises and async/await were introduced to solve.

---

### 9. What is the difference between `module.exports` and `exports` in Node.js?

**Answer:** In Node's CommonJS module system, both start out pointing to the **same object** — `exports` is just a reference/shorthand to `module.exports`.

```js
// Both work the same way here:
exports.foo = 'bar';
module.exports.foo = 'bar';
```

**The gotcha:** if you **reassign** `exports` directly to a new object, it breaks the reference — the module will still export whatever `module.exports` points to, ignoring your reassigned `exports`.

```js
// WRONG — this does NOT work as expected:
exports = { foo: 'bar' }; // exports now points to a new object, module.exports is unaffected
// The module actually exports {} (or whatever module.exports originally was)

// CORRECT:
module.exports = { foo: 'bar' }; // this is the object actually returned by require()
```
**Rule of thumb:** if exporting a single function/class/object (replacing the whole export), always use `module.exports =`. Use `exports.name = ` only when attaching multiple named properties without reassigning the whole object.

---

### 10. What are the main differences between Node.js and JavaScript in the browser?

**Answer:**

| Aspect | Browser JS | Node.js |
|---|---|---|
| Global object | `window` | `global` |
| DOM/BOM APIs | Available (`document`, `window`, `localStorage`) | Not available — no DOM |
| Module system | ES Modules natively (`<script type="module">`) | CommonJS (`require`) traditionally, ES Modules also supported now |
| File system access | None (sandboxed for security) | Full access via `fs` module |
| Networking | `fetch`, `XMLHttpRequest`, restricted by CORS | `http`/`https` modules, no CORS restriction (server-to-server) |
| Threading model | Single-threaded + Web Workers | Single-threaded event loop + Worker Threads/child processes |
| Use case | Client-side UI/interactivity | Server-side logic, APIs, tooling, CLIs |

Both run on the same underlying language (ECMAScript) and, notably, both Node and Chrome use the **V8 engine** — but they expose entirely different sets of host APIs appropriate to their environment (DOM/browser APIs vs. OS/file system/networking APIs).

---

## INTERMEDIATE LEVEL

### 1. What is clustering in Node.js?

**Answer:** Since Node runs JavaScript on a **single thread**, a single Node process can only use **one CPU core**, no matter how many cores the machine has. **Clustering** (via the built-in `cluster` module) solves this by forking multiple **worker processes**, each running its own instance of the Node app, all sharing the same server port. The OS (or Node's internal round-robin scheduler) distributes incoming connections across these worker processes.

```js
const cluster = require('cluster');
const os = require('os');

if (cluster.isPrimary) {
  const numCPUs = os.cpus().length;
  for (let i = 0; i < numCPUs; i++) cluster.fork();

  cluster.on('exit', (worker) => {
    console.log(`Worker ${worker.process.pid} died, restarting...`);
    cluster.fork(); // restart on crash — improves resilience too
  });
} else {
  require('./server'); // each worker runs the actual Express app
}
```

**Why it's used:** to fully utilize multi-core machines (throughput scales roughly with core count for I/O-bound workloads) and to improve resilience — if one worker crashes, others keep serving traffic while the primary process restarts the failed one.

**Caveat to mention:** workers don't share memory — in-memory state (e.g., an in-process cache or session store) isn't shared across workers, so you need an external store (Redis) for anything that needs to be consistent across all workers. In production, this role is often handled by a process manager like **PM2** or by container orchestration (Kubernetes running multiple pod replicas) instead of the raw `cluster` module.

---

### 2. How does Node.js handle child processes?

**Answer:** The `child_process` module lets Node spawn separate OS processes — useful for running shell commands, other executables, or offloading CPU-heavy work outside the main event loop.

- **`exec(command, callback)`**: runs a command in a shell, buffers the **entire** stdout/stderr in memory, and returns it via callback once the process exits. Good for short-lived commands with small output (e.g., `git status`). Risky for large output since it's all buffered in memory.
- **`spawn(command, args)`**: launches a command **without** a shell (by default) and returns a **stream-based** interface (`stdout`/`stderr` are Readable streams) — better for long-running processes or large output, since you can process data incrementally instead of waiting for it all to buffer.
- **`fork(modulePath)`**: a specialized version of `spawn` specifically for **spawning new Node.js processes**, with a built-in IPC (inter-process communication) channel so the parent and child can `send()`/`on('message')` to each other. Commonly used to offload CPU-heavy JS work to a separate process while keeping the main server responsive.

```js
const { spawn } = require('child_process');
const ls = spawn('ls', ['-lh', '/usr']);
ls.stdout.on('data', (data) => console.log(`stdout: ${data}`));
ls.on('close', (code) => console.log(`child exited with code ${code}`));

const { fork } = require('child_process');
const child = fork('./heavy-task.js');
child.send({ task: 'generateReport' });
child.on('message', (result) => console.log('Result from child:', result));
```

---

### 3. What are Node.js buffers?

**Answer:** A `Buffer` is a fixed-size chunk of **raw binary data** allocated outside the V8 JS heap. JS strings are UTF-16 encoded and immutable, and aren't well-suited for handling binary data (image bytes, TCP packet data, file contents before encoding is known). Buffers exist to handle this efficiently.

```js
const buf = Buffer.from('hello', 'utf-8');
console.log(buf); // <Buffer 68 65 6c 6c 6f> — raw byte representation
console.log(buf.toString('utf-8')); // 'hello' — convert back to string

const buf2 = Buffer.alloc(10); // allocates 10 zeroed-out bytes
```

**Key differences from strings:**
- Buffers are **mutable** (you can modify individual bytes); strings are immutable.
- Buffers store **raw bytes**, with no inherent character encoding until you interpret them (`.toString('utf-8')`, `.toString('base64')`, etc.) — this matters when handling file uploads, network sockets, or crypto operations where you're dealing with data before you know/decide its text encoding.
- Buffers live outside the V8 heap, which avoids some GC pressure for large binary payloads.

**Common use case:** reading a file/network stream returns `Buffer` chunks by default (not strings) — you either work with them as bytes or explicitly decode them.

---

### 4. What are some common design patterns in Node.js?

**Answer:**

- **Singleton**: ensure only one instance of something exists (e.g., a single database connection pool shared across the app). Node's module caching naturally supports this — `require('./db')` returns the same cached instance every time it's imported.
```js
// db.js
class Database { /* ... */ }
module.exports = new Database(); // same instance shared everywhere it's required
```

- **Factory**: a function/class that creates and returns objects without exposing the exact instantiation logic to the caller — useful when object creation is conditional or complex (e.g., creating different payment gateway clients based on config).
```js
function createPaymentClient(provider) {
  if (provider === 'stripe') return new StripeClient();
  if (provider === 'adyen') return new AdyenClient();
  throw new Error('Unknown provider');
}
```

- **Observer**: an object (subject) maintains a list of listeners and notifies them of events — Node's built-in `EventEmitter` is a direct implementation of this pattern, used pervasively (streams, HTTP servers, custom domain events like `orderCreated`).
```js
const emitter = new EventEmitter();
emitter.on('orderCreated', (order) => sendConfirmationEmail(order));
emitter.emit('orderCreated', order);
```

- **Also worth mentioning if pressed further:** **Middleware pattern** (Express — chain of responsibility), **Module pattern** (CommonJS's default encapsulation via `module.exports`), **Dependency Injection** (heavily used in NestJS via decorators/constructor injection).

---

### 5. What are CORS and how do you enable it in Express.js?

**Answer:** **CORS (Cross-Origin Resource Sharing)** is a browser security mechanism that blocks a web page from making requests to a different origin (different domain/protocol/port) than the one it was served from, **unless** the server explicitly allows it via response headers. This exists to prevent malicious sites from silently making authenticated requests to other sites on a user's behalf.

Node itself doesn't enforce CORS (it's a browser-side restriction) — but as the **server**, you need to send the right headers for the browser to allow the response through to the calling frontend.

```js
const cors = require('cors');

// Allow all origins (fine for public APIs, not for anything requiring credentials)
app.use(cors());

// Restrict to a specific origin, with credentials (cookies/auth headers)
app.use(cors({
  origin: 'https://shop.example.com',
  credentials: true,
}));
```
Manually, this is equivalent to setting headers like `Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Credentials` on responses (and correctly handling the browser's preflight `OPTIONS` request for non-simple requests).

---

### 6. What is the purpose of the `package-lock.json` file?

**Answer:** `package.json` declares dependency ranges (e.g., `"express": "^4.18.0"`, meaning "any compatible 4.x version ≥ 4.18.0"). This flexibility is a problem for **reproducibility** — two different `npm install` runs, days apart, could resolve to different exact versions if new compatible releases were published in between.

`package-lock.json` locks down the **exact resolved version** (and the entire dependency tree, including nested dependencies' exact versions) at the time of install. Committing this file ensures every developer, CI pipeline, and production deploy installs the **exact same dependency tree**, eliminating "works on my machine" bugs caused by version drift.

**Best practice:** always commit `package-lock.json` to version control, and use `npm ci` (not `npm install`) in CI/CD pipelines — `npm ci` installs strictly from the lockfile and fails if `package.json`/lockfile are out of sync, rather than silently updating things.

---

### 7. What is an EventEmitter in Node.js?

**Answer:** `EventEmitter` (from the built-in `events` module) is the core building block behind Node's event-driven architecture — it implements the **Observer pattern**, letting objects emit named events that other code can subscribe to.

```js
const EventEmitter = require('events');

class OrderService extends EventEmitter {
  createOrder(data) {
    const order = { id: '123', ...data };
    // ... save to DB ...
    this.emit('orderCreated', order); // notify any listeners
    return order;
  }
}

const orderService = new OrderService();
orderService.on('orderCreated', (order) => {
  console.log(`Sending confirmation email for order ${order.id}`);
});
orderService.on('orderCreated', (order) => {
  console.log(`Notifying inventory service about order ${order.id}`);
});

orderService.createOrder({ productId: 'abc' });
// Both listeners fire, decoupled from the order creation logic itself
```
Many core Node modules (HTTP servers, streams, `process`) are themselves `EventEmitter`s under the hood (`req.on('data', ...)`, `server.on('connection', ...)`). Understanding EventEmitter is foundational to understanding most of Node's async APIs.

---

### 8. How does error handling work in Node.js?

**Answer:** Node has a few distinct error-handling contexts depending on whether code is synchronous, callback-based, or Promise-based:

**1. Synchronous code — `try/catch`:**
```js
try {
  JSON.parse(invalidJson);
} catch (err) {
  console.error('Parse failed:', err.message);
}
```

**2. Callback-based async code — "error-first callback" convention:** the first argument to a callback is reserved for an error (or `null` if none).
```js
fs.readFile('file.txt', (err, data) => {
  if (err) return console.error(err); // must explicitly check — try/catch does NOT catch async callback errors
  console.log(data);
});
```
**Important gotcha:** wrapping an async callback-based call in `try/catch` does **not** catch errors that occur inside the callback itself, since the callback runs later, outside the original synchronous call stack.

**3. Promises/async-await — `.catch()` or `try/catch` around `await`:**
```js
async function getOrder(id) {
  try {
    const order = await db.orders.findById(id);
    return order;
  } catch (err) {
    logger.error('Failed to fetch order', err);
    throw err; // re-throw or handle, depending on context
  }
}
```

**4. Event-based errors (EventEmitter/streams):** by convention, error conditions are emitted as an `'error'` event. **If there's no listener for `'error'` on an EventEmitter, Node throws the error and crashes the process** — so always attach an error listener on streams/emitters that might fail.
```js
readStream.on('error', (err) => console.error('Stream failed:', err));
```

**5. Centralized handling in Express:** a 4-argument middleware `(err, req, res, next)` placed last catches errors passed via `next(err)`, giving one place for consistent error logging/response formatting.

**6. Process-level safety nets:** `process.on('uncaughtException', ...)` and `process.on('unhandledRejection', ...)` — these should be used to **log and gracefully shut down**, not to "recover" and keep running, since the process may be in an inconsistent state after an uncaught error.

---

### 9. What is the difference between `require` and `import`?

**Answer:**
- **`require`** is Node's original **CommonJS** module syntax. It's **synchronous** (loading happens immediately, blocking until the module is loaded) and dynamic (you can `require()` conditionally, inside an `if` block, with a computed path).
- **`import`** is the **ES Modules (ESM)** standard syntax (part of the JS language spec, not Node-specific). It's **static** by default (import statements must be at the top level, so tooling can statically analyze the dependency graph — enabling tree-shaking) and Node loads ESM **asynchronously** under the hood.

```js
// CommonJS
const express = require('express');
module.exports = router;

// ES Modules
import express from 'express';
export default router;
```

**Interop notes worth mentioning:**
- Node supports both today — `.cjs`/`.mjs` extensions, or `"type": "module"` in `package.json` to treat `.js` files as ESM by default.
- Dynamic `import()` (returns a Promise) works even in CommonJS files, useful for lazy-loading a module.
- Named exports work differently: CommonJS attaches everything to a single `module.exports` object; ESM has genuinely distinct named vs. default exports enforced by the spec.
- Many modern frontend bundlers/TS setups default to ESM syntax even when the underlying execution is transpiled to CommonJS — worth clarifying which the actual project uses if asked in an interview about "have you used ESM."

---

### 10. What are the pros and cons of using Node.js for backend development?

**Answer:**

**Pros:**
- **Single language** across frontend and backend (JS/TS) — shared types, shared validation logic, easier context-switching for full-stack developers.
- **Excellent for I/O-bound workloads** (APIs, real-time apps) due to the non-blocking event loop — high concurrency with relatively low memory overhead per connection compared to thread-per-request models.
- **Massive ecosystem (npm)** — huge library availability speeds up development.
- **Fast to prototype and iterate** — dynamic typing (optionally strict with TS), quick startup, good for microservices.
- Strong for **real-time features** (WebSockets, Socket.IO) given the event-driven model.

**Cons:**
- **Poor fit for CPU-intensive work** (image/video processing, heavy computation, complex synchronous algorithms) since it blocks the single JS thread — needs worker threads or offloading to another service/language.
- **Callback/async complexity**: while async/await has improved this significantly, async control flow can still be a source of bugs (unhandled rejections, forgetting `await`) for less experienced developers.
- **Immature typing without TypeScript**: raw JS lacks compile-time safety — most serious Node backends now use TypeScript to mitigate this, which is effectively considered a near-requirement for production codebases now.
- **Callback-style legacy libraries** can still exist in older codebases/dependencies, mixing paradigms.
- Error handling requires **discipline** (as covered in Q8) — an uncaught error in an unexpected place can crash the whole process, affecting every in-flight request, unlike some multi-process-per-request server models where one request's crash doesn't affect others.

---

## ADVANCED LEVEL

### 1. How does Node.js handle concurrency with its single-threaded model?

**Answer:** Node achieves concurrency **without** multi-threading JS execution by exploiting the fact that most server workloads are **I/O-bound, not CPU-bound** — the server spends most of its time waiting on network/disk/database responses, not computing.

**Mechanism:**
1. JS itself runs on a single thread (the "main thread").
2. When an I/O operation is initiated (DB query, file read, HTTP call), Node hands it off to the underlying system — for network I/O, the OS's async I/O primitives (epoll/kqueue/IOCP) are used directly; for file system operations (which don't have great cross-platform async OS primitives), libuv uses a **thread pool** (default 4 threads) to simulate async behavior.
3. The main thread is immediately free to process other incoming requests/events while waiting.
4. When the I/O completes, its callback is queued, and the event loop picks it up on the main thread when it's free.

This gives you **concurrency** (handling many requests "at once," interleaved) without true **parallelism** for JS code execution (only one piece of JS logic runs at any given instant). For genuine parallel *computation*, you need worker threads, child processes, or horizontal scaling (multiple Node processes/clustering).

**Interview framing:** "Node is concurrent but not parallel by default for JS execution — it's exceptional at juggling many waiting operations, but a single long-running synchronous computation will still block everything else."

---

### 2. What are Worker Threads in Node.js?

**Answer:** The `worker_threads` module allows you to run **actual JavaScript in parallel**, on separate OS threads, each with its own V8 instance and event loop — unlike the main event loop's I/O delegation, this gives genuine parallelism for **CPU-bound** JS code.

```js
// main.js
const { Worker } = require('worker_threads');

const worker = new Worker('./heavy-computation.js', {
  workerData: { numbers: largeArray },
});
worker.on('message', (result) => console.log('Result:', result));
worker.on('error', (err) => console.error(err));

// heavy-computation.js
const { parentPort, workerData } = require('worker_threads');
const result = workerData.numbers.reduce((sum, n) => sum + expensiveCalc(n), 0);
parentPort.postMessage(result);
```

**Worker Threads vs. Clustering — the key distinction:**
| | Worker Threads | Clustering |
|---|---|---|
| Isolation | Threads within the **same process**, can share memory via `SharedArrayBuffer` | Fully separate **processes**, no shared memory |
| Use case | Offload a specific **CPU-heavy task** without blocking the main event loop | Scale an entire **server app** across CPU cores for handling more concurrent connections |
| Overhead | Lighter weight than spawning full processes | Heavier — each worker is a full Node process |
| Communication | Message passing, or shared memory buffers | Message passing (IPC) only, no shared memory |

**When to reach for which:** clustering = "I want more capacity to handle concurrent HTTP requests." Worker threads = "I have one specific expensive computation (image resizing, PDF generation, large data transformation) that's blocking my event loop, and I want to run it off the main thread without spinning up a whole separate process/service."

---

### 3. How do you secure a Node.js application?

**Answer:** Key practices to mention (interviewers often want breadth here, not depth on every point):

- **Input sanitization/validation**: never trust client input — validate/sanitize using libraries like `joi`, `zod`, or `class-validator` (NestJS). Prevents injection attacks and malformed data from corrupting business logic.
- **Prevent SQL/NoSQL injection**: use parameterized queries/prepared statements (never string-concatenate user input into queries) or an ORM that does this by default (Prisma, TypeORM, Mongoose with proper query construction).
- **XSS (Cross-Site Scripting) prevention**: escape/sanitize any user-generated content rendered back in HTML; set proper `Content-Security-Policy` headers; use frameworks (React) that escape by default rather than raw `innerHTML`.
- **CSRF (Cross-Site Request Forgery) prevention**: use CSRF tokens for state-changing requests from browser sessions, or rely on `SameSite` cookie attributes; less of a concern for pure token-based APIs (mobile/SPA with bearer tokens) but critical for cookie-based session auth.
- **Environment variables for secrets**: never hardcode API keys/DB credentials in code — use `.env` files (via `dotenv`) locally and a proper secrets manager (AWS Secrets Manager, Vault) in production; never commit `.env` to version control.
- **Use HTTPS/TLS** everywhere, including internal service-to-service calls where feasible.
- **Rate limiting**: prevent brute-force/abuse (e.g., `express-rate-limit`), especially important on auth endpoints and — in a commerce context — checkout/payment endpoints (card-testing fraud).
- **Dependency security**: run `npm audit` regularly, use tools like Snyk/Dependabot to catch known vulnerabilities in dependencies.
- **Helmet.js**: sets a collection of sensible security-related HTTP headers by default (`X-Content-Type-Options`, `X-Frame-Options`, etc.) with one line: `app.use(helmet())`.
- **Least privilege**: DB users/service accounts should have only the permissions they actually need, not broad admin access.
- **Proper auth**: hash passwords with a strong algorithm (`bcrypt`/`argon2`, never plain MD5/SHA1), use short-lived JWTs with refresh token rotation, validate JWT signatures/expiry on every request.

---

### 4. What is the `libuv` library in Node.js?

**Answer:** `libuv` is a **C library** that Node.js is built on top of, providing the **event loop** and **asynchronous, cross-platform I/O** capabilities. It abstracts away OS-specific differences in how async I/O is done (Linux's epoll, macOS's kqueue, Windows' IOCP), giving Node a consistent async I/O API regardless of platform.

**Its core responsibilities:**
1. **The event loop itself** — the phases (timers, poll, check, etc.) described earlier are literally implemented in libuv.
2. **Thread pool** (default size 4, configurable via `UV_THREADPOOL_SIZE`) — used for operations that don't have good native async OS support, like most **file system operations**, some **DNS lookups** (`dns.lookup`), and certain **crypto** functions (`crypto.pbkdf2`, `bcrypt`'s async methods).
3. **Networking** — TCP/UDP socket handling, using native async OS mechanisms directly (no thread pool needed here, since OSes have good native async networking support).

**Why this distinction matters in an interview:** it explains *why* file system operations can exhaust the thread pool under heavy load (only 4 threads by default handling all fs/crypto/DNS work) while network I/O scales much further without that bottleneck — a nuanced point that shows deeper Node knowledge if you can articulate it.

---

### 5. How does the `process` module work in Node.js?

**Answer:** `process` is a **global object** (no `require` needed) providing information about, and control over, the current Node.js process.

**Commonly used members:**
```js
// process.env — access environment variables (config, secrets, feature flags)
const dbUrl = process.env.DATABASE_URL;
const isProduction = process.env.NODE_ENV === 'production';

// process.argv — command-line arguments passed when starting the script
// e.g., `node app.js --port 3000` → process.argv = ['node', 'app.js', '--port', '3000']
const port = process.argv[3];

// process.on — listen for process-level events
process.on('exit', (code) => console.log(`Process exiting with code ${code}`));
process.on('uncaughtException', (err) => {
  logger.error('Uncaught exception:', err);
  process.exit(1); // fail fast rather than continue in an unknown state
});
process.on('unhandledRejection', (reason) => {
  logger.error('Unhandled rejection:', reason);
});
process.on('SIGTERM', () => {
  // graceful shutdown — e.g., Kubernetes sends SIGTERM before killing a pod
  server.close(() => process.exit(0));
});

// Other useful members:
process.exit(code);      // terminate the process immediately with an exit code
process.cwd();            // current working directory
process.memoryUsage();    // heap/RSS memory stats — useful for debugging leaks
process.hrtime();         // high-resolution timer, useful for precise performance measurement
```
**Commerce-relevant example:** graceful shutdown handling (`SIGTERM`) is important in containerized environments — you want in-flight checkout/payment requests to finish before the process dies during a deployment, rather than being abruptly cut off mid-transaction.

---

### 6. What is the difference between middleware and controllers in Express.js?

**Answer:**
- **Middleware**: functions that run **in the request pipeline**, generally performing cross-cutting concerns that apply broadly (logging, auth checks, body parsing, CORS, rate limiting). Middleware typically either calls `next()` to pass control along, or short-circuits the response. It's not meant to contain the core business logic of a specific endpoint.
- **Controllers**: the functions that handle the actual **business logic for a specific route** — e.g., `getOrderById`, `createOrder`. They receive the (already processed by middleware) `req`/`res` and are responsible for producing the final response for that specific endpoint.

```js
// Middleware — generic, reusable across many routes
function authMiddleware(req, res, next) {
  if (!req.headers.authorization) return res.status(401).end();
  req.user = decodeToken(req.headers.authorization);
  next();
}

// Controller — specific business logic for one route
function getOrderController(req, res) {
  const order = orderService.findById(req.params.id, req.user.id);
  res.json(order);
}

app.get('/orders/:id', authMiddleware, getOrderController);
```
**Mental model:** middleware = "things that should happen for many/all requests before the real work" (a pipeline). Controllers = "the actual work for this specific endpoint." In larger apps (or NestJS), you also typically add a **service layer** between controllers and data access, so controllers stay thin (just handling req/res) and business logic lives in testable service classes.

---

### 7. Explain how Node.js manages memory.

**Answer:** Node (via V8) manages memory primarily through **automatic garbage collection (GC)**, using a **generational** approach:

- **Young generation ("new space")**: newly created objects go here first. Most objects die young (short-lived), so this is collected frequently using a fast, cheap algorithm ("Scavenge" — copies live objects to a new space, everything else is reclaimed).
- **Old generation ("old space")**: objects that survive multiple young-gen collections get "promoted" here. This is collected less frequently but with a more thorough (and more expensive) algorithm ("Mark-Sweep-Compact").

**Common causes of memory leaks in Node (interviewers love this question):**
1. **Global variables** accumulating data indefinitely (e.g., an unbounded in-memory cache/array that keeps growing).
2. **Closures** unintentionally retaining references to large objects longer than needed.
3. **Uncleared timers/intervals** (`setInterval` that's never `clearInterval`'d) holding references alive.
4. **Event listeners not removed** — e.g., attaching a listener inside a function that's called repeatedly without ever calling `.removeListener()`/`.off()`, causing listeners (and whatever they close over) to accumulate.
5. **Detached objects held by long-lived collections** — e.g., a `Map` used as a cache with no eviction policy (no TTL, no max size, no LRU eviction) growing unbounded over the app's lifetime.

**How to detect/debug leaks in practice:**
- `process.memoryUsage()` to monitor heap growth over time.
- Node's `--inspect` flag + Chrome DevTools heap snapshots — take snapshots at different points, compare, look for growing object counts of a particular type.
- `--max-old-space-size` flag to set/observe heap limits; production monitoring (e.g., Datadog, New Relic) tracking RSS/heap trends over time to catch slow leaks before they cause an OOM crash.

---

### 8. What are HTTP/2 streams in Node.js?

**Answer:** HTTP/2 introduced **multiplexing** — the ability to send **multiple concurrent request/response pairs over a single TCP connection**, each represented as an independent **stream** with a unique ID. This is a major improvement over HTTP/1.1, where each connection could really only handle one request at a time efficiently (leading browsers to open multiple parallel TCP connections as a workaround, each with its own overhead).

**Advantages over HTTP/1.1:**
- **No head-of-line blocking at the HTTP layer** — one slow response doesn't block others sharing the same connection (though this can still occur at the TCP layer under packet loss).
- **Header compression (HPACK)** — reduces overhead from repeated headers across many requests.
- **Server push** (though largely deprecated/removed in modern browsers due to caching complications) — allowed a server to proactively send resources before the client asked.
- Fewer total TCP connections needed → less connection-setup overhead, especially valuable on high-latency networks.

**Node's `http2` module:**
```js
const http2 = require('http2');
const server = http2.createSecureServer({ key, cert }); // HTTP/2 requires TLS in practice

server.on('stream', (stream, headers) => {
  stream.respond({ ':status': 200, 'content-type': 'application/json' });
  stream.end(JSON.stringify({ message: 'hello' }));
});
```
**Practical note for an interview:** most Node apps today sit behind a reverse proxy/load balancer/CDN (nginx, ALB, Cloudflare) that terminates HTTP/2 externally and speaks HTTP/1.1 internally to the Node app — so direct use of Node's raw `http2` module is less common than knowing *why* HTTP/2 matters at the infrastructure level.

---

### 9. What are some performance optimization techniques in Node.js?

**Answer:**

- **Clustering / horizontal scaling**: utilize all CPU cores (or run multiple container replicas) rather than a single Node process handling everything.
- **Caching**: cache expensive/frequent computations or DB query results in Redis/in-memory (with proper invalidation) to avoid redundant work — e.g., caching computed product pricing or catalog data that doesn't change every request.
- **Database query optimization**: proper indexing, avoiding N+1 query patterns (batch/join instead of looping individual queries), using pagination for large result sets, connection pooling to avoid the overhead of creating a new DB connection per request.
- **Gzip/Brotli compression**: compress HTTP responses (`compression` middleware in Express) to reduce payload size over the wire, especially for large JSON responses or static assets.
- **Avoid blocking the event loop**: move CPU-heavy work to worker threads or a separate service; avoid synchronous file/crypto operations in request handlers.
- **Streaming large responses** instead of building the entire payload in memory first (e.g., stream a large CSV export directly to the response rather than building the full string first).
- **Efficient serialization**: avoid unnecessary `JSON.stringify`/`parse` of huge objects on hot paths; consider more efficient formats (protobuf) for internal service-to-service communication if payload size/parsing cost becomes a bottleneck.
- **Load testing and profiling**: use tools like `autocannon`, `clinic.js`, or Node's built-in `--prof` flag to identify actual bottlenecks before optimizing — avoid guessing at performance problems.
- **Connection keep-alive**: reuse HTTP connections (both incoming and for outbound calls to other services/DBs) rather than paying connection setup cost repeatedly.

---

### 10. How would you handle real-time communication in Node.js?

**Answer:** For real-time, bidirectional communication (as opposed to traditional request-response), the main options are:

- **WebSockets** (raw `ws` library, or the native `WebSocket` API): a persistent, full-duplex connection between client and server — either side can push data at any time without the client having to poll or re-request. Lower-level than Socket.IO — you handle reconnection, message framing, etc. yourself (or via additional libraries).

- **Socket.IO**: a library built on top of WebSockets (with automatic fallback to HTTP long-polling if WebSockets aren't available, e.g., behind certain restrictive proxies) that adds convenient abstractions: automatic reconnection, "rooms" (group broadcasting), acknowledgements, and a simpler event-based API (`socket.emit`, `socket.on`).

```js
const io = require('socket.io')(server);

io.on('connection', (socket) => {
  socket.join(`order:${orderId}`); // join a "room" scoped to a specific order

  socket.on('disconnect', () => console.log('Client disconnected'));
});

// Elsewhere, e.g., when payment webhook confirms an order:
io.to(`order:${orderId}`).emit('orderStatusUpdated', { status: 'paid' });
// Any client subscribed to this order's room gets a live update — e.g., "your order was just confirmed" without polling
```

**Scenarios where this applies (commerce-relevant):**
- Live order status updates (e.g., "your payment is processing... confirmed!") without the client polling an endpoint repeatedly.
- Live inventory/stock updates on a product page (e.g., "only 2 left!" updating in real time as other users purchase).
- Live chat/customer support widgets.
- Live auction/bidding-style features if relevant to the domain.

**Scaling consideration worth mentioning:** WebSocket connections are **stateful and stick to a specific server instance** — when running multiple Node instances behind a load balancer, you need either **sticky sessions** (route a client's requests consistently to the same instance) or a shared pub/sub layer (e.g., **Redis adapter for Socket.IO**) so that an event emitted from one instance (e.g., the instance that received the payment webhook) can be broadcast to a client connected to a *different* instance.
