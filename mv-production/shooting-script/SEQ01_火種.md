# SEQ01 — 火種・開場 (The Spark)

> **Intro ｜ 0.0–16.0s ｜ f0–384 (24fps) ｜ 7 shots**
> 歌詞：*Yo! Shift the gear, we're moving in! / The PropNex life, let the growth begin! / Forget the noise, forget the fake, / We're building up for all that's at stake!*
> 音樂：前奏漸起，能量 0.16→0.40。**鼓點落在 f0、f48、f96、f144…**（143BPM ≈ 每拍 10.07 幀，本段以視覺鼓點 f0/f48/f96/f168/f240/f312 為主卡點）。
> 段落目標：用「光」立下全片母題；四老闆＝起源；光鳥＝Sharpen the Wing；以一扇被點亮的窗交棒給主角。

---

## SHOT 1.01 — 火種呼吸 (Orb Breathing)
- **■ TC** f0–96 ｜ 0.0–4.0s ｜ Dur 96f
- **■ SEQ/SCENE** SEQ01 ｜ INT 虛空 VOID ｜ 無時間（前世界）
- **■ SIZE/LENS** ECU 大特寫 ｜ 100mm macro 等效 ｜ T2.0（極淺景深）｜ 對焦：火種核心
- **■ CAMERA** 正面平視，靜止機位 + 呼吸手持噪波(±1.5px)；f48–96 極緩推近 1.00→1.04（ease-in）
- **■ STAGING** 火種置於畫面中心略偏黃金點(x0.5,y0.46)；周圍 30% 半徑內有可見體積霧與 8–12 顆浮塵；其餘全黑
- **■ ACTION（四層）**
  - f0–10〔主〕全黑→火種隨第一鼓點(f0)亮起到 60% 亮度，core 直徑 18px
  - f10–28〔主〕亮度 60%→30%（第一次「吐氣」），core 內部粒子順時針對流
  - f28–48〔主〕30%→85%（吸氣，對齊 f48 鼓點），bloom 外擴
  - f48–72〔主〕85%→45%（吐氣）
  - f72–96〔主〕45%→100%（最大吸氣，準備交棒下鏡）
  - 全程〔次〕浮塵被火種微弱氣流帶動，做布朗式漂移（速度 ≤ 3px/s）
  - 全程〔微〕core 邊緣有 2px 抖動的能量絲；霧層以 0.5px/f 緩慢翻滾
  - 全程〔環境〕火種亮起時，周圍霧被照亮（GI），暗時轉回深藍黑
- **■ FX** 火種＝emissive volume + 內部 curl-noise 粒子(~2000)；體積霧(VDB 低密度)；bloom/glow 在 comp
- **■ LIGHT** 唯一光源＝火種自發光；無補光；霧層接收 single-scatter；色溫核心 6500K→邊緣暖 3000K
- **■ COLOR** 黑底 `#0A2540`(底)→`#06101C`(角落)；火心 `#0070E0`→`#FFF4D6`；冷暖比 全暗場僅火種暖核
- **■ AUDIO** 第一鼓點/低頻 boom @f0 對火種亮起；f48 副拍對第二次吸氣；環境 SFX：低頻嗡鳴 + 微弱「心跳」
- **■ EDIT** 開場淡入（前 6f 由純黑 0%→100%）；尾接 1.02 用「亮度峰交接」（火種最亮時 cut）
- **■ ASSETS** spark_core(emissive) · dust_particles · fog_vdb
- **■ RENDER** emission / volume / Z-depth / cryptomatte；雜訊門檻 < 0.01（暗場易見螢火蟲，採樣加倍）
- **■ NOTE** 火種的「呼吸節奏」是全片心跳母題，記住此曲線，SEQ08 北極星要呼應同一節奏

---

## SHOT 1.02 — 四老闆共護火種 (The Four)
- **■ TC** f96–168 ｜ 4.0–7.0s ｜ Dur 72f
- **■ SEQ/SCENE** SEQ01 ｜ INT 虛空→2018空辦公室交界 ｜ 起源
- **■ SIZE/LENS** WS 遠景 ｜ 28mm ｜ T2.8 ｜ 對焦：四人剪影，火種輕微失焦發光
- **■ CAMERA** 微仰 5°，從火種特寫**接續 dolly-out**（1.04→1.0 焦距感），f96–168 後退 + 緩降，露出四人全身剪影
- **■ STAGING** 四人對稱站位（左二右二），火種懸於四人手間中央；前景左下角放一張虛化辦公桌角(占畫面15%)增加縱深；背景極遠處有 2018 城市夜景虛化光點
- **■ 人物定位（剪影逆光，不露清晰五官）**
  - 左外：Steve（行動派，重心微前）｜左內：Marcus（最高、最穩，CEO 中心感）
  - 右內：Evon（手勢將啟）｜右外：Yuki（略柔，髮絲飄）
- **■ ACTION**
  - f96–120〔主〕鏡頭後退露出四人；四人幾乎靜止但「活」：各自呼吸起伏(胸腔1px)
  - f120–144〔次〕Marcus 重心由右腳→雙腳(微轉)；Yuki 一縷髮絲被氣流吹起(cloth/hair sim)
  - f144–168〔主〕四人同時把手再向火種靠攏 2cm（為下鏡 insert 鋪陳，match-on-action）
  - 全程〔微〕四人輪廓光隨火種呼吸明滅(GI)；衣料褶皺隨微動產生次級晃動
  - 全程〔環境〕浮塵在四人之間的光束中浮游
- **■ FACE** 剪影僅見側臉輪廓光；眼神皆望向火種（eyeline 收束於中心）；不需精細表情
- **■ FX** 逆光輪廓的體積光束(4 道，自火種射向鏡頭被四人遮擋形成 god-ray 縫隙)；浮塵
- **■ LIGHT** 火種為唯一 key（背逆光）；四人正面僅 5% 環境補光保留輪廓；rim 強、face 暗（純剪影）
- **■ COLOR** navy 剪影 `#0A2540`；火種藍金邊光描邊四人輪廓；冷暖比 9:1（極暗，僅中心暖）
- **■ AUDIO** f96 弦樂/pad 進場墊底；歌詞前奏氛圍；無台詞
- **■ EDIT** 接 1.01「亮度峰」cut；接 1.03 用「手靠攏動作」match-on-action
- **■ ASSETS** founder_rigs ×4（剪影 LOD 即可，臉部低模）· desk_corner_prop · city_bokeh_card
- **■ RENDER** beauty / volume(god-ray) / cryptomatte（四人各一 ID 供 comp 微調）
- **■ NOTE** 四老闆是真人，**此鏡用剪影逆光可規避肖像精度問題**，但站位/體型仍需符合本人特徵；正式露臉留待 SEQ07-08

---

## SHOT 1.03 — 四手靠近火種 (Hands · Insert)
- **■ TC** f168–210 ｜ 7.0–8.75s ｜ Dur 42f
- **■ SEQ/SCENE** SEQ01 ｜ 火種特寫 ｜ 起源
- **■ SIZE/LENS** CU 特寫(insert) ｜ 85mm ｜ T2.2 ｜ 對焦：火種與最近指尖
- **■ CAMERA** 俯角 25°，靜止 + 極輕呼吸；無推拉（insert 沉穩）
- **■ STAGING** 火種在中央下方(y0.55)；四隻手從畫框四角斜伸入，指尖距火種約一個火種直徑，不觸碰；手緣處於焦外漸糊
- **■ ACTION**
  - f168–186〔主〕承接 1.02，四指尖再靠近(共 1.5cm)，火種感應而漲亮 +15%
  - f186–200〔微〕指節皮膚因動作產生微皺；指尖被火光照亮處有暖 SSS 透紅
  - f200–210〔主〕四手定住（moving hold：仍有 0.5px 呼吸微動），火種在掌心間脈動一次
  - 全程〔環境〕火光在四掌心反射(GI 暖斑)，掌紋細節可見
- **■ FACE** 無（純手部）
- **■ FX** 火種 emissive 微增；掌心 GI 暖反射
- **■ LIGHT** 火種 key 由下往上打亮手掌（戲劇性 under-light）；指縫漏光
- **■ COLOR** 暖膚色 + 藍金火光；此鏡暖比上升到 4:6（手被照暖）
- **■ AUDIO** 歌詞氛圍延續；加一記輕「叮」SFX 對火種脈動(f200)
- **■ EDIT** match-on-action 接 1.02；接 1.04 連續（同機位微推進）
- **■ ASSETS** hand_rigs ×4(高模含指甲/皮膚 micro-displacement) · spark_core
- **■ RENDER** beauty / SSS / emission / AO（掌心接縫陰影）
- **■ NOTE** 皮膚 SSS 是 Soul 級溫暖感關鍵；耳/指透光要做出血色

---

## SHOT 1.04 — 手收攏・火種漲亮 (Swell)
- **■ TC** f210–252 ｜ 8.75–10.5s ｜ Dur 42f
- **■ SEQ/SCENE** SEQ01 ｜ 火種特寫 ｜ 起源
- **■ SIZE/LENS** CU ｜ 85mm ｜ T2.2 ｜ 對焦：火種核心（手退焦外）
- **■ CAMERA** 同 1.03 機位，f210–252 緩推 1.0→1.08（ease-in-out），手逐漸退出畫框上緣
- **■ ACTION**
  - f210–228〔主〕四手做「放開前的最後收攏」後**緩緩抽離**，火種失去包覆開始自由漲大
  - f228–245〔主〕火種直徑 18px→34px，亮度衝到 120%（過曝核心），內部粒子加速旋轉
  - f245–252〔主〕火種開始「拉長」變形，下緣冒出第一根能量羽——預示光鳥（anticipation）
  - 全程〔次〕抽離的手在畫框邊緣有殘影動態模糊
  - 全程〔環境〕霧被強光推開一圈(體積位移)，浮塵被吹散
- **■ FX** 火種 emissive 漲大 + 過曝 bloom；curl 粒子加速；霧的 push-out；羽狀能量 wisp 萌生
- **■ LIGHT** 火種增亮使全畫面短暫提亮 0.5EV（自動曝光感，comp 處理）
- **■ COLOR** 藍金，高光趨近 `#FFF4D6`；過曝邊緣暖白溢出
- **■ AUDIO** 音樂能量上拔(pre-roll)；上升 whoosh SFX 起頭，對 f245 變形
- **■ EDIT** 連續推進接 1.05（不切，或極短 6f dissolve 強調形變）
- **■ ASSETS** spark_core(可變形) · hand_rigs(退場) · fog_vdb
- **■ NOTE** 這顆是「火種→光鳥」的轉化醞釀，變形要有「生命要誕生」的張力，別只是放大

---

## SHOT 1.05 — 火種化光鳥 (Bird Forms)
- **■ TC** f252–312 ｜ 10.5–13.0s ｜ Dur 60f
- **■ SEQ/SCENE** SEQ01 ｜ 虛空→城市上空交界 ｜ 起源
- **■ SIZE/LENS** CU→MS ｜ 50mm ｜ T2.8 ｜ 對焦：成形中的鳥（focus pull 隨後拉）
- **■ CAMERA** 由特寫**跟拍後拉**（鳥成形時鏡頭隨之拉開，1.08→0.85），輕微弧線上移
- **■ KEYS（hero 鏡・關鍵姿勢）**
  | 幀 | pose |
  |----|------|
  | f252 | 火種長條狀，下緣兩根羽 wisp 初現 |
  | f264 | 能量向兩側展開＝雛翅；頭部光點分化 |
  | f276 | 鳥形 70% 成形，翅半開，尾羽流出 |
  | f288 | 完整光鳥懸停，雙翅向下「預備」（anticipation，蓄力） |
  | f300 | 雙翅向上抬到最高點（將振） |
  | f312 | 翅停在高點(接 1.06 振翅) |
- **■ ACTION**
  - f252–276〔主〕火種能量重組為鳥（粒子流向羽翼結構）
  - f276–288〔次〕成形瞬間灑落火星粒子（fall-off sparks）
  - f288–312〔主〕光鳥懸停、雙翅做一次預備下壓→上抬（為振翅蓄勢）
  - 全程〔微〕鳥體 emissive 呼吸；羽緣能量絲飄動
  - 全程〔環境〕鳥的光照亮殘餘霧與下方城市輪廓開始浮現
- **■ FX** 粒子重組(form-up)；火星灑落；能量拖尾雛形；體積光
- **■ LIGHT** 光鳥成為移動 key 光源，照亮環境；背景城市開始以剪影出現
- **■ COLOR** 藍金光鳥 vs 漸現的 navy 夜城；拖尾 bloom
- **■ AUDIO** whoosh 收束 + 一聲清亮「鳥鳴/風鈴」音色對 f288 成形；音樂前奏推向人聲
- **■ EDIT** 接 1.04 連續；接 1.06「振翅動作」match-on-action
- **■ ASSETS** lightbird_rig(含翅/尾羽 IK + emissive) · formup_particles · city_silhouette(LOD remote)
- **■ NOTE** 光鳥造型＝曲名 Sharpen the Wing 母題，**全片會重複出現**(SEQ04/07)，此處定下其飛行語彙與光色

---

## SHOT 1.06 — 光鳥磨翅振翅 (Sharpen the Wing)
- **■ TC** f312–348 ｜ 13.0–14.5s ｜ Dur 36f
- **■ SEQ/SCENE** SEQ01 ｜ 城市上空 ｜ 夜
- **■ SIZE/LENS** MS ｜ 50mm ｜ T2.8 ｜ 對焦：光鳥
- **■ CAMERA** 微仰跟拍，f312–348 隨鳥輕微上移 + 輕微 roll(2°) 增加飛翔動感
- **■ KEYS**
  | 幀 | pose |
  |----|------|
  | f312 | 雙翅高位(承接1.05) |
  | f318 | 翅「磨利」：翅尖能量收束成銳利刃狀(sharpen 視覺化) |
  | f324 | 強力下振(power stroke)，身體上拔，拖尾爆發 |
  | f334 | 翅收至最低、身體達最高，速度線 streak |
  | f342 | 翅再展開滑翔 |
  | f348 | 滑翔姿，準備掠向城市(接1.07) |
- **■ ACTION**
  - f312–318〔主〕翅尖能量「磨亮」收銳——這是 hook 視覺，與後續副歌重複一致
  - f318–334〔主〕一記有力下振，身體竄高(weight & intent)；拖尾在 f324 爆量
  - f334–348〔次〕滑翔，羽緣能量絲後曳；速度殘影(motion blur 強)
  - 全程〔環境〕下方城市被掠過的光照亮一道移動亮帶
- **■ FX** 翅尖 sharpen 能量收束 FX；power-stroke 拖尾爆發；速度線/動態模糊
- **■ LIGHT** 鳥光掃過城市產生 sweeping highlight
- **■ COLOR** 藍金為主，下振瞬間核心更亮(`#FFF4D6`)
- **■ AUDIO** ★對音樂卡點：下振(f324)對前奏一記強拍/鈸；whoosh
- **■ EDIT** match-on-action 接 1.07（滑翔方向延續）
- **■ ASSETS** lightbird_rig · trail_FX · city(LOD)
- **■ NOTE** 記下「磨翅→下振→上拔」三拍節奏曲線；SEQ04.06 與 SEQ07.01 要 reuse 同一動作 DNA

---

## SHOT 1.07 — 掠夜城・點亮一窗 (Light the Window)
- **■ TC** f348–384 ｜ 14.5–16.0s ｜ Dur 36f
- **■ SEQ/SCENE** SEQ01 ｜ EXT 2018 吉隆坡夜空 ｜ 夜
- **■ SIZE/LENS** WS 大遠景 ｜ 24mm ｜ T4.0(較深，看清城市) ｜ 對焦：中景樓宇/目標窗
- **■ CAMERA** **crane up + 前推**，航拍感；光鳥為前景引導線由左上掠向右下的目標大樓
- **■ STAGING** 三層縱深：前景—光鳥拖尾掠過；中景—公寓樓群(目標窗在右下黃金點)；遠景—雙子塔剪影 + 體積雲微光。城市車流光點移動
- **■ ACTION**
  - f348–366〔主〕光鳥俯衝掠過樓群，拖尾劃出弧線
  - f366–378〔主〕光鳥俯衝點觸目標窗——該窗由暗`#1d2731`「啪」地亮起暖光`#E9A23B`
  - f378–384〔主〕光鳥拉起飛離出框上緣；鏡頭微推向那扇亮窗（為轉場 SEQ02 鋪陳）
  - 全程〔次〕拖尾粒子飄散；雲層緩飄；車流光點移動(crowd of lights)
  - 全程〔環境〕點亮的窗向外溢一圈暖光，鄰近 2–3 扇窗微微反光
- **■ FACE** 無
- **■ FX** 光鳥拖尾；窗亮起的 bloom 脈衝；體積雲；城市車流光點 instancing
- **■ LIGHT** 光鳥移動 key；目標窗亮起＝新 practical 暖光源誕生（敘事：信念抵達主角）
- **■ COLOR** navy 夜空 + 城市冷白點光 + 目標窗暖橘 + 光鳥藍金；暖點在冷海中第一次出現
- **■ AUDIO** ★f366 窗亮 對前奏收束/人聲將進的「起音」；輕「叮」+ 漸入人聲氣口
- **■ EDIT** **轉場到 SEQ02**：鏡頭推向亮窗 → SEQ02.01 由窗內接出（match cut，窗的暖光連戲）
- **■ ASSETS** lightbird_rig · KL_skyline(雙子塔) · apartment_block(目標窗 practical) · cloud_vdb · car_light_instancer
- **■ RENDER** beauty / emission(窗+鳥) / volume(雲) / Z-depth(景深) / motion-vector
- **■ NOTE** 目標窗＝阿凱阿俊的辦公室窗，位置/造型要與 SEQ02 室內場景**對得上**（同一扇窗的內外）

---

## SEQ01 交付檢查 (Sequence QC)
- [ ] 火種呼吸節奏(1.01)與北極星(SEQ08)節奏一致
- [ ] 四老闆站位/體型符合本人特徵（即使剪影）
- [ ] 光鳥「磨翅→下振→上拔」動作 DNA 建立，供 SEQ04/07 reuse
- [ ] 1.07 目標窗 與 SEQ02.01 室內窗 內外連戲
- [ ] 全段唯一光源邏輯成立（火種→光鳥→窗），無穿幫補光
- [ ] f366 窗亮卡到人聲起音
