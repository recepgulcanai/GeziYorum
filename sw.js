// Cep Rehberi çevrimdışı önbellek. Sürüm, içerik değişince otomatik değişir.
const CACHE='cep-rehberi-a8cb07e3';
const FILES=["./", "index.html", "data.js", "manifest.webmanifest", "icon-192.png", "icon-512.png", "icon-180.png", "img/harita-bratislava.webp", "img/harita-budapeste.webp", "img/harita-parndorf.webp", "img/harita-prag.webp", "img/harita-viyana.webp"];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==CACHE).map(x=>caches.delete(x)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET'||new URL(e.request.url).origin!==location.origin)return;
  // Önce ağ (güncel içerik), olmazsa önbellek: internet yokken de açılır.
  e.respondWith(fetch(e.request).then(r=>{const c=r.clone();caches.open(CACHE).then(x=>x.put(e.request,c));return r}).catch(()=>caches.match(e.request,{ignoreSearch:true}).then(r=>r||caches.match('index.html'))));
});
