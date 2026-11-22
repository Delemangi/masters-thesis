// Serves the built deck (dist/) on http://localhost:8080 with no dependencies, so it works offline.
import { createServer } from 'node:http'
import { readFile } from 'node:fs/promises'
import { extname, join, normalize } from 'node:path'
import { fileURLToPath } from 'node:url'
import { exec } from 'node:child_process'

const root = join(fileURLToPath(new URL('.', import.meta.url)), 'dist')
const port = Number(process.env.PORT) || 8080
const types = {
  '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2', '.woff': 'font/woff',
  '.mp4': 'video/mp4', '.ico': 'image/x-icon',
}

createServer(async (req, res) => {
  const path = normalize(decodeURIComponent(new URL(req.url, 'http://x').pathname)).replace(/^([/\\])+/, '')
  const file = join(root, path || 'index.html')
  if (!file.startsWith(root)) { res.writeHead(403).end(); return }
  try {
    const body = await readFile(file)
    res.writeHead(200, { 'Content-Type': types[extname(file)] || 'application/octet-stream' }).end(body)
  } catch {
    const body = await readFile(join(root, 'index.html'))
    res.writeHead(200, { 'Content-Type': 'text/html' }).end(body)
  }
}).listen(port, () => {
  const url = `http://localhost:${port}/`
  console.log(`Presentation running at ${url}  (presenter view: ${url}#/presenter/1)  Ctrl+C to stop.`)
  if (!process.env.NO_OPEN) exec(process.platform === 'win32' ? `start "" "${url}"` : `open "${url}"`)
})
