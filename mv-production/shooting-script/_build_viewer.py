#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html, glob, os

SRC = "/home/user/PNXMarketing/mv-production/shooting-script"
OUT = os.path.join(SRC, "viewer.html")

SEQS = [
    ("01","火種・開場","Intro","0:00–0:16","f0–384",7,"#0A2540","#0070E0",
     "Yo! Shift the gear… let the growth begin!"),
    ("02","留下來的人","Verse 1a","0:16–0:30","f384–720",10,"#3a4658","#566370",
     "Real life results… learning deep / world is fast asleep."),
    ("03","沒人看好","Verse 1b","0:30–0:44","f720–1056",11,"#2c3742","#566370",
     "Project, Sub-sales… every chapter is a bridge you burn."),
    ("04","不停前進・蛻變","Chorus 1 ★","0:44–1:15","f1056–1800",16,"#0070E0","#E9A23B",
     "We evolve, we create! …sharpen the wing! …Think Big!"),
    ("05","建立","Verse 2","1:15–1:46","f1800–2544",16,"#0070E0","#00AEEF",
     "flipping the home… no lone wolves… education daily."),
    ("06","家・傳承","Bridge","1:46–1:57","f2544–2808",7,"#E9A23B","#FFF4D6",
     "a family foundation… the kinder the soul."),
    ("07","遍佈全馬・燈海","Chorus 2 ★","1:57–2:25","f2808–3480",16,"#0070E0","#E9A23B",
     "…Turning the thousands to millions for us!"),
    ("08","願景・北極星","Outro","2:25–2:33","f3480–3672",6,"#FFF4D6","#E9A23B",
     "PropNex! Good to Great! Think Big! …Let's go!"),
]
FIELD_FULL = {"ACTION","KEYS","STAGING","NOTE"}  # render full-width

def esc(s): return html.escape(s, quote=False)

def fmt_inline(s):
    s = esc(s)
    s = s.replace("★", '<span class="star">★</span>')
    s = s.replace("⚠️", '<span class="warn">⚠️</span>')
    # frame refs f123 / f123–456
    s = re.sub(r'(f\d+(?:–\d+)?)', r'<span class="fr">\1</span>', s)
    # layer tags 〔主〕〔次〕〔微〕〔環境〕
    s = re.sub(r'〔(主)〕', r'<span class="ly ly1">主</span>', s)
    s = re.sub(r'〔(次)〕', r'<span class="ly ly2">次</span>', s)
    s = re.sub(r'〔(微)〕', r'<span class="ly ly3">微</span>', s)
    s = re.sub(r'〔(環境)〕', r'<span class="ly ly4">環境</span>', s)
    # hex colors -> swatch
    s = re.sub(r'(#[0-9A-Fa-f]{6})', r'<span class="hex"><i style="background:\1"></i>\1</span>', s)
    # **bold**
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s

def render_value(lines):
    """lines: list of raw text lines (already stripped of the field marker on first)."""
    out=[]; tbl=[]; bullets=[]
    def flush_tbl():
        nonlocal tbl
        if not tbl: return
        rows=[r for r in tbl if not re.match(r'^\s*\|[\s:|-]+\|\s*$', r)]
        html_rows=[]
        for i,r in enumerate(rows):
            cells=[c.strip() for c in r.strip().strip('|').split('|')]
            tag='th' if i==0 else 'td'
            html_rows.append('<tr>'+''.join(f'<{tag}>{fmt_inline(c)}</{tag}>' for c in cells)+'</tr>')
        out.append('<table class="kf">'+''.join(html_rows)+'</table>')
        tbl=[]
    def flush_b():
        nonlocal bullets
        if not bullets: return
        out.append('<ul class="bl">'+''.join(f'<li>{fmt_inline(b)}</li>' for b in bullets)+'</ul>')
        bullets=[]
    for ln in lines:
        s=ln.strip()
        if not s: continue
        if s.startswith('|'):
            flush_b(); tbl.append(s); continue
        else:
            flush_tbl()
        if s.startswith('- '):
            bullets.append(s[2:].strip())
        else:
            flush_b(); out.append(f'<p>{fmt_inline(s)}</p>')
    flush_tbl(); flush_b()
    return ''.join(out)

def parse_seq(path):
    txt=open(path,encoding='utf-8').read().split('\n')
    meta=[]; shots=[]; qc=[]
    i=0; n=len(txt)
    # intro blockquote
    while i<n and not txt[i].startswith('# '): i+=1
    i+=1
    while i<n and (txt[i].startswith('>') or txt[i].strip()=='' ):
        if txt[i].startswith('>'): meta.append(txt[i].lstrip('> ').rstrip())
        i+=1
    cur=None
    while i<n:
        ln=txt[i]
        m=re.match(r'^#{2,3}\s+(SHOT\s+[\d.–\-]+)\s*[—\-]\s*(.+)$', ln)
        mqc=re.match(r'^##\s+.*(交付檢查|Sequence QC)', ln)
        if mqc:
            cur=None; i+=1
            while i<n:
                s=txt[i].strip()
                if s.startswith('- ['): qc.append(re.sub(r'^- \[.\]\s*','',s))
                elif s.startswith('## '): break
                i+=1
            continue
        if m:
            cur={'no':m.group(1).replace('SHOT ','').strip(),'title':m.group(2).strip(),'fields':[],'note':''}
            shots.append(cur); i+=1
            # capture any leading '>' note (group wrapper)
            while i<n and txt[i].strip().startswith('>'):
                cur['note']+= txt[i].strip().lstrip('> ')+' '; i+=1
            continue
        fm=re.match(r'^-\s*\*\*■\s*(.+?)\*\*(.*)$', ln)
        if fm and cur is not None:
            fname=fm.group(1).strip(); rest=fm.group(2).strip()
            vlines=[rest] if rest else []
            i+=1
            while i<n:
                nx=txt[i]
                if re.match(r'^-\s*\*\*■', nx) or re.match(r'^#{1,3}\s', nx): break
                vlines.append(nx)
                i+=1
            cur['fields'].append((fname,vlines))
            continue
        i+=1
    return meta, shots, qc

def field_label(name):
    cn=name.split('（')[0].split('(')[0].strip()
    return cn

CARDS={}
for s in SEQS:
    num=s[0]
    f=glob.glob(os.path.join(SRC,f"SEQ{num}_*.md"))
    if not f: continue
    CARDS[num]=parse_seq(f[0])

# ---------- emit HTML ----------
def seq_section(s):
    num,title,part,tc,frames,nshots,c1,c2,lyric=s
    meta,shots,qc=CARDS.get(num,([], [], []))
    cards=[]
    for sh in shots:
        if not sh['fields']:
            # group divider
            note=f'<div class="grp"><span class="gno">{esc(sh["no"])}</span> {esc(sh["title"])} <em>{fmt_inline(sh["note"].strip())}</em></div>'
            cards.append(note); continue
        # header chips from TC/SIZE
        tcv=size=cam=''
        body=[]
        for fname,vlines in sh['fields']:
            lab=field_label(fname)
            val=render_value(vlines)
            if lab=='TC': tcv=' '.join(vlines).strip()
            if lab in ('SIZE/LENS',): size=' '.join(vlines).strip()
            if lab=='CAMERA': cam=' '.join(vlines).strip()
            full=' full' if lab in FIELD_FULL else ''
            body.append(f'<div class="fld{full}"><span class="flab">{esc(lab)}</span><div class="fval">{val}</div></div>')
        star=' has-star' if '★' in sh['title'] or '★' in tcv else ''
        chips=''
        if tcv: chips+=f'<span class="chip tc">{fmt_inline(tcv)}</span>'
        if size: chips+=f'<span class="chip">{esc(size.split("｜")[0].strip())}</span>'
        cards.append(f'''<div class="shot{star}" id="s{esc(sh["no"])}">
          <div class="shead"><span class="sno">{esc(sh["no"])}</span>
            <h4>{fmt_inline(sh["title"])}</h4>{chips}</div>
          <div class="sgrid">{''.join(body)}</div></div>''')
    metahtml=''.join(f'<div class="mline">{fmt_inline(m)}</div>' for m in meta if m)
    qchtml=''
    if qc:
        qchtml='<div class="qc"><div class="qct">Sequence QC · 交付檢查</div>'+''.join(f'<label><input type="checkbox"> {fmt_inline(q)}</label>' for q in qc)+'</div>'
    return f'''<section class="seq" id="seq{num}">
      <div class="seqhead" style="background:linear-gradient(100deg,{c1}cc,{c2}55)">
        <div class="seqno">{num}</div>
        <div class="seqmeta"><div class="seqt">{esc(title)}</div>
          <div class="seqsub"><span>{esc(part)}</span><span>{esc(tc)}</span><span>{esc(frames)}</span><span>{nshots} shots</span></div>
          <div class="seqly">“{esc(lyric)}”</div></div>
      </div>
      <div class="seqintro">{metahtml}</div>
      <div class="shots">{''.join(cards)}</div>
      {qchtml}
    </section>'''

nav=''.join(f'<a href="#seq{s[0]}">{s[0]} {esc(s[1].split("・")[0])}</a>' for s in SEQS)
strip=''
total=3672
for s in SEQS:
    a,b=re.findall(r'\d+', s[4])
    w=(int(b)-int(a))/total*100
    st='star' if '★' in s[3] else ''
    strip+=f'<a href="#seq{s[0]}" class="seg {st}" style="width:{w:.3f}%;background:linear-gradient(180deg,{s[6]},{s[7]})"><b>{s[0]}</b><i>{esc(s[3].replace(" ★",""))}</i></a>'
sections=''.join(seq_section(s) for s in SEQS)

HTML=f'''<!DOCTYPE html><html lang="zh-Hant"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>PropNex · Sharpen the Wing — Shooting Script Viewer</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700;800;900&family=DM+Serif+Display&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{{--navy:#0A2540;--blue:#0070E0;--sky:#00AEEF;--amber:#E9A23B;--gold:#FFF4D6;--grey:#566370;
--paper:#070f1a;--card:#0e1c2e;--card2:#122438;--line:rgba(255,255,255,.10);--line2:rgba(255,255,255,.2);
--t1:#EAF2FB;--t2:#9DB2C9;--t3:#6E859E;--mono:'JetBrains Mono',monospace}}
*{{margin:0;padding:0;box-sizing:border-box}}
html{{scroll-behavior:smooth}}
body{{font-family:'DM Sans',sans-serif;background:var(--paper);color:var(--t1);line-height:1.6;font-size:15px;-webkit-font-smoothing:antialiased}}
.serif{{font-family:'DM Serif Display',serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 24px}}
a{{color:inherit;text-decoration:none}}
/* nav */
.nav{{position:sticky;top:0;z-index:60;background:rgba(7,15,26,.9);backdrop-filter:blur(16px);border-bottom:1px solid var(--line)}}
.nav-i{{max-width:1180px;margin:0 auto;display:flex;align-items:center;gap:4px;overflow-x:auto;scrollbar-width:none;padding:11px 24px}}
.nav-i::-webkit-scrollbar{{display:none}}
.nav-i .lg{{font-family:'DM Serif Display',serif;font-size:16px;margin-right:8px;white-space:nowrap}}
.nav-i .lg b{{color:var(--sky)}}
.nav-i a{{white-space:nowrap;font-size:12px;font-weight:600;color:var(--t2);padding:6px 11px;border-radius:18px}}
.nav-i a:hover{{color:#fff;background:rgba(0,112,224,.22)}}
/* hero */
.hero{{padding:64px 0 30px;position:relative;overflow:hidden}}
.hero-bg{{position:absolute;inset:0;background:radial-gradient(700px 400px at 80% 10%,rgba(0,174,239,.18),transparent 60%),radial-gradient(600px 400px at 10% 90%,rgba(233,162,59,.13),transparent 60%),linear-gradient(160deg,#06101c,#0a1c30)}}
.hero .wrap{{position:relative}}
.kick{{display:inline-flex;gap:8px;align-items:center;font-size:11px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--sky);border:1px solid var(--line2);padding:7px 14px;border-radius:30px;margin-bottom:18px}}
.hero h1{{font-size:clamp(34px,6vw,64px);line-height:1;color:#fff;letter-spacing:-.02em}}
.hero h1 em{{font-style:italic;color:var(--sky)}}
.hero p{{color:var(--t2);margin-top:14px;max-width:680px}}
.specs{{display:flex;gap:8px;flex-wrap:wrap;margin-top:22px}}
.specs span{{font-size:12px;font-weight:600;background:rgba(255,255,255,.05);border:1px solid var(--line);padding:7px 12px;border-radius:8px}}
.specs span i{{color:var(--t3);font-style:normal}}
/* film strip */
.strip{{display:flex;gap:3px;margin-top:26px;height:62px;border-radius:10px;overflow:hidden}}
.seg{{position:relative;display:flex;flex-direction:column;justify-content:flex-end;padding:7px 8px;min-width:30px;transition:.2s;opacity:.86}}
.seg:hover{{opacity:1;transform:translateY(-2px)}}
.seg b{{font-family:'DM Serif Display',serif;font-size:16px;color:#fff;text-shadow:0 1px 4px rgba(0,0,0,.6)}}
.seg i{{font-size:9px;color:rgba(255,255,255,.85);font-style:normal;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.seg.star::after{{content:"★";position:absolute;top:5px;right:6px;color:#fff;font-size:11px}}
/* sequence */
.seq{{padding:42px 0 10px;border-top:1px solid var(--line)}}
.seqhead{{display:flex;align-items:center;gap:18px;border-radius:14px;padding:18px 22px;border:1px solid var(--line)}}
.seqno{{font-family:'DM Serif Display',serif;font-size:50px;color:#fff;line-height:.8;opacity:.92}}
.seqt{{font-size:23px;font-weight:800;color:#fff}}
.seqsub{{display:flex;gap:10px;flex-wrap:wrap;margin:5px 0}}
.seqsub span{{font-size:11.5px;font-weight:700;color:#fff;background:rgba(0,0,0,.28);padding:3px 9px;border-radius:7px}}
.seqly{{font-size:13px;color:rgba(255,255,255,.92);font-style:italic}}
.seqintro{{margin:14px 0 6px;padding:14px 18px;background:var(--card);border:1px solid var(--line);border-radius:12px}}
.mline{{font-size:13px;color:var(--t2);padding:2px 0}}
.mline b{{color:var(--t1)}}
/* shots */
.shots{{display:flex;flex-direction:column;gap:14px;margin-top:14px}}
.grp{{font-size:13px;color:var(--t2);padding:8px 14px;background:rgba(255,255,255,.03);border-left:3px solid var(--sky);border-radius:6px}}
.grp .gno{{font-family:var(--mono);font-weight:700;color:var(--sky)}}
.grp em{{font-style:normal;color:var(--t3)}}
.shot{{background:linear-gradient(180deg,var(--card),var(--paper));border:1px solid var(--line);border-radius:14px;overflow:hidden}}
.shot.has-star{{border-color:rgba(233,162,59,.5);box-shadow:0 0 0 1px rgba(233,162,59,.2)}}
.shead{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:14px 18px;border-bottom:1px solid var(--line);background:rgba(255,255,255,.02)}}
.sno{{font-family:var(--mono);font-weight:700;font-size:13px;color:var(--navy);background:var(--sky);padding:4px 9px;border-radius:7px}}
.shead h4{{font-size:16px;color:#fff;flex:1;min-width:120px}}
.chip{{font-size:11px;font-weight:600;color:var(--t2);background:rgba(255,255,255,.05);border:1px solid var(--line);padding:4px 9px;border-radius:7px}}
.chip.tc{{font-family:var(--mono);color:var(--gold)}}
.sgrid{{display:grid;grid-template-columns:1fr 1fr;gap:0}}
.fld{{padding:11px 18px;border-top:1px solid rgba(255,255,255,.05);border-right:1px solid rgba(255,255,255,.05)}}
.fld.full{{grid-column:1/-1}}
.flab{{display:inline-block;font-size:10px;font-weight:800;letter-spacing:.08em;color:var(--sky);background:rgba(0,112,224,.12);padding:2px 7px;border-radius:5px;margin-bottom:6px}}
.fval{{font-size:13px;color:var(--t1)}}
.fval p{{margin:2px 0}}
.fval .bl{{margin:2px 0 2px 4px;list-style:none}}
.fval .bl li{{position:relative;padding-left:14px;margin:3px 0;font-size:12.5px;color:var(--t1)}}
.fval .bl li::before{{content:"";position:absolute;left:2px;top:8px;width:4px;height:4px;border-radius:50%;background:var(--t3)}}
.fr{{font-family:var(--mono);font-size:11.5px;color:var(--gold);background:rgba(255,244,214,.08);padding:0 4px;border-radius:4px}}
.ly{{font-size:10px;font-weight:800;padding:1px 5px;border-radius:4px;margin:0 2px}}
.ly1{{background:#0070E0;color:#fff}} .ly2{{background:#00AEEF;color:#04243a}}
.ly3{{background:#566370;color:#fff}} .ly4{{background:#E9A23B;color:#3a2606}}
.hex{{display:inline-flex;align-items:center;gap:4px;font-family:var(--mono);font-size:11px;color:var(--t2)}}
.hex i{{width:10px;height:10px;border-radius:3px;border:1px solid var(--line2);display:inline-block}}
.star{{color:var(--amber);font-weight:800}}
.warn{{filter:saturate(1.4)}}
table.kf{{border-collapse:collapse;margin:6px 0;width:100%;font-size:12px}}
table.kf th{{text-align:left;color:var(--sky);font-weight:700;padding:4px 8px;border-bottom:1px solid var(--line);background:rgba(0,112,224,.08)}}
table.kf td{{padding:4px 8px;border-bottom:1px solid rgba(255,255,255,.05);color:var(--t1);vertical-align:top}}
table.kf td:first-child{{font-family:var(--mono);color:var(--gold);white-space:nowrap}}
.qc{{margin:14px 0 4px;padding:14px 18px;background:rgba(0,174,239,.06);border:1px solid rgba(0,174,239,.25);border-radius:12px}}
.qct{{font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--sky);margin-bottom:8px}}
.qc label{{display:block;font-size:13px;color:var(--t2);padding:3px 0;cursor:pointer}}
.qc input{{margin-right:8px;accent-color:var(--sky)}}
.foot{{padding:50px 0;text-align:center;color:var(--t3);font-size:12.5px;border-top:1px solid var(--line);margin-top:30px}}
.foot .serif{{font-size:20px;color:#fff;margin-bottom:8px}}
.legend{{display:flex;gap:14px;flex-wrap:wrap;justify-content:center;margin-top:12px;font-size:11px;color:var(--t3)}}
@media(max-width:760px){{.sgrid{{grid-template-columns:1fr}} .seqno{{font-size:38px}} .hero h1{{font-size:34px}}}}
</style></head><body>
<nav class="nav"><div class="nav-i"><span class="lg">Prop<b>Nex</b> · Shooting Script</span>{nav}</div></nav>
<header class="hero"><div class="hero-bg"></div><div class="wrap">
  <span class="kick">● Production Shooting Script · Frame-Accurate · v1.0</span>
  <h1 class="serif">Sharpen the <em>Wing</em></h1>
  <p>製作級・逐幀拍攝腳本檢視器。全片 <b style="color:#fff">153.0s / 3,672 幀 / 24fps / 89 顆鏡頭</b>。每顆鏡頭含運鏡曲線、四層動作、關鍵姿勢、FX/燈光/調色/音樂卡點與資產 render 註記。</p>
  <div class="specs"><span><i>FPS</i> 24</span><span><i>Res</i> 4K UHD</span><span><i>Color</i> ACEScg→Rec709</span><span><i>Shots</i> 89</span><span><i>Frames</i> 3,672</span><span><i>★ 卡點</i> f1056 · f2808</span></div>
  <div class="strip">{strip}</div>
  <div class="legend"><span><span class="ly ly1">主</span> 主動作</span><span><span class="ly ly2">次</span> 次動作</span><span><span class="ly ly3">微</span> 微動作</span><span><span class="ly ly4">環境</span> 環境反應</span><span><span class="fr">f###</span> 幀</span><span><span class="star">★</span> 最強卡點</span></div>
</div></header>
<div class="wrap">{sections}</div>
<footer class="foot"><div class="wrap"><div class="serif">Sharpen the Wing</div>
<p>PropNex Malaysia · Frame-Accurate Shooting Script · 89 shots / 3,672 frames @ 24fps</p>
<p style="margin-top:6px;color:#3f4f63">人名為佔位、四位老闆肖像需簽核。Good to Great · Think Big · 事業成功，家庭幸福</p>
</div></footer>
</body></html>'''

open(OUT,'w',encoding='utf-8').write(HTML)
print("wrote", OUT, len(HTML), "bytes")
# quick stats
import collections
tot=sum(len([1 for sh in CARDS[k][1] if sh['fields']]) for k in CARDS)
print("shot cards:", tot)
