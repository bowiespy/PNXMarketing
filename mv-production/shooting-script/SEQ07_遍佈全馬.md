# SEQ07 — 遍佈全馬・燈海 (2000 Strong) ★

> **Chorus 2 / 大副歌 ｜ 117.0–145.0s ｜ f2808–3480 (24fps) ｜ 16 shots**
> 歌詞：*(Chorus 重複) We don't just rise, we evolve, we create! …sharpen the wing! …Think Big! …Turning the thousands to millions for us!*
> 音樂：能量 0.61→0.67（**全片最高峰**）。★大副歌落點 = f2808 (1:57)。
> 段落目標：視覺與情緒總爆發。個人燈火→全馬燈海→太空→俯衝回六人群像。

---

## SHOT 7.01 — 穿雲・全馬點燈 ★ (Pierce the Clouds)
- **■ TC** f2808–2868 ｜ 117.0–119.5s ｜ Dur 60f ｜ WS ｜ 18mm ｜ T5.6 ｜ ★最強卡點
- **■ SEQ/SCENE** EXT 雲層之上→俯瞰城市群・夜
- **■ CAMERA** **crane 穿雲接俯衝**，超廣角航拍；f2808 由 SEQ06 燈火爆量接入
- **■ KEYS** f2808 穿出雲層/f2820 下方第一城燈點亮/f2844 燈點連鎖向四方擴散/f2868 城市群燈海初成
- **■ ACTION**
  - f2808–2820〔主〕鏡頭穿出體積雲層，露出腳下夜城
  - f2820–2868〔主〕城市一盞盞藍金燈接連亮起(連鎖擴散)；〔次〕光鳥領頭穿越雲縫；雲被氣流撕開
- **■ FX** 體積雲穿越;燈點連鎖;光鳥拖尾;雲撕裂
- **■ LIGHT** 萬家燈火＝大量點光源;雲接收下方燈光輝映
- **■ COLOR** navy 夜 + 藍金燈點爆亮 + 雲體積光
- **■ AUDIO** ★f2808 大副歌 downbeat;弦樂/鼓全開;whoosh
- **■ EDIT** 光接光 match 接 SEQ06.07;接 7.02
- **■ ASSETS** cloud_vdb · city_lights_instancer · lightbird_rig
- **■ RENDER** beauty / volume(雲) / emission(燈) / Z-depth / motion-vector
- **■ NOTE** ★全片第二大卡點;穿雲的「破繭而出」要爽;誤差 ≤2 幀

---

## SHOT 7.02 — 城市燈點連鎖亮 (Cities Light Up)
- **■ TC** f2868–2904 ｜ 119.5–121.0s ｜ Dur 36f ｜ WS ｜ 24mm ｜ 空拍
- **■ ACTION** 空拍持續,更多城市/城鎮燈點如漣漪向外連鎖點亮;〔環境〕道路如發光血管串起城市
- **■ FX** 燈點連鎖 + 道路光帶
- **■ COLOR** 藍金燈海擴張
- **■ AUDIO** "We don't just rise, we evolve";EDIT 接 7.03
- **■ ASSETS** city_lights_instancer · road_glow
- **■ NOTE** 從點→線→面的擴散邏輯,呼應公司「遍佈全馬」

---

## SHOT 7.03 — 人潮光河 (Crowd · River of Light)
- **■ TC** f2904–2964 ｜ 121.0–123.5s ｜ Dur 60f ｜ MS ｜ 35mm ｜ T2.8 ｜ 群眾 oner
- **■ CAMERA** **oner 從人群中穿行再升起**,淺→深景深變化;hero 角色近景穿插
- **■ ACTION**
  - f2904–2934〔主〕地面廣場萬人舉燈,鏡頭穿行人潮,每人一盞藍金燈匯成流動光河
  - f2934–2964〔次〕人群揮手、跟唱、旗幟橫幅動(crowd staggered);鏡頭升起露出光河規模
- **■ FACE** 近景 hero 激動含淚笑
- **■ FX** crowd sim(2000 agents) + 燈海粒子 + 光河流動
- **■ LIGHT** 藍金燈海 + 舞台光
- **■ COLOR** 藍金燈海、暖金為主
- **■ AUDIO** "Turning the Good to the legendary Great";萬人合唱底
- **■ EDIT** 接 7.04
- **■ ASSETS** crowd_2000(LOD instancing) · lantern_FX · stage_set
- **■ NOTE** 2000 人＝公司今日規模;遠景 impostor/粒子、近景 hero 精修

---

## SHOT 7.04 — Hero 同唱 hook (Sing the Hook · Lip-sync)
- **■ TC** f2964–3000 ｜ 123.5–125.0s ｜ Dur 36f ｜ CU ｜ 85mm ｜ T2.0 ｜ 微推
- **■ ACTION** 幾位 hero agent(含阿凱阿俊)張口同唱副歌 hook;〔微〕舉燈、含淚、髮絲動
- **■ FACE** 對嘴(visemes 對 "sharpen the wing");激動真摯
- **■ AUDIO** ★"gotta sharpen the wing"(可對嘴);EDIT 接 7.05
- **■ ASSETS** hero_agent_rigs · kai_rig · jun_rig
- **■ NOTE** 對外片要好跟唱;hook 句做精準對嘴方便現場帶動

---

## SHOT 7.05 — 地標亮燈 (Landmarks Light)
- **■ TC** f3000–3036 ｜ 125.0–126.5s ｜ Dur 36f ｜ WS ｜ 24mm ｜ 微仰
- **■ ACTION** 吉隆坡雙子塔等地標由下而上逐層亮燈;〔環境〕煙花光點升騰
- **■ FX** 地標逐層亮 + 煙花
- **■ COLOR** navy + 地標藍金光
- **■ AUDIO** "When you look at the vision";EDIT 接 7.06
- **■ ASSETS** KL_landmarks(雙子塔等) · firework_FX
- **■ NOTE** 地標＝馬來西亞識別;授權確認地標使用無虞(或做風格化)

---

## SHOT 7.06 — 光字「67→2000」(Light Words)
- **■ TC** f3036–3084 ｜ 126.5–128.5s ｜ Dur 48f ｜ WS ｜ 35mm ｜ 跟
- **■ ACTION** f3036–3060〔主〕"67 → 2000" 與 "Thousands to Millions" 藍金光字在天空粒子書寫;f3060–3084〔次〕光字飄散成燈點融入燈海
- **■ FX** 光字 write-on + 飄散
- **■ COLOR** navy + 藍金光字 bloom
- **■ AUDIO** ★"Think Big" / "thousands to millions" 對光字
- **■ EDIT** 接 7.07
- **■ ASSETS** light_text_FX
- **■ NOTE** SEQ04.14 數字母題的放大版;67→2000 是公司核心成長數據

---

## SHOT 7.07 — 煙花光粒升騰 (Fireworks)
- **■ TC** f3084–3132 ｜ 128.5–130.5s ｜ Dur 48f ｜ WS ｜ 28mm ｜ 靜
- **■ ACTION** 城市上空煙花/光粒升騰綻放、與燈海呼應;〔環境〕水面/玻璃帷幕反射光斑(caustics)
- **■ FX** 煙花粒子 + 反射焦散
- **■ COLOR** 藍金為主、暖金煙花
- **■ AUDIO** 大副歌高潮;EDIT 接 7.08
- **■ ASSETS** firework_FX · city_reflective
- **■ NOTE** 慶典感;FX 與地標/水面互動

---

## SHOT 7.08 — 衛星視角・全馬燈海 ★ (Satellite · Think Big)
- **■ TC** f3132–3192 ｜ 130.5–133.0s ｜ Dur 60f ｜ WS ｜ 太空 ｜ 升旋
- **■ KEYS** f3132 升出大氣/f3152 馬來西亞輪廓浮現/f3172 半島+東馬燈海連片/f3192 整國發光
- **■ ACTION**〔主〕鏡頭升至太空,馬來西亞地圖(含東馬沙巴砂拉越)整片被藍金燈海覆蓋;〔環境〕大氣輝光脈動、雲流動
- **■ FX** 地圖燈海 + 大氣輝光 + 雲層
- **■ LIGHT** 深空暗 + 國土燈海自發光
- **■ COLOR** 深空 navy + 馬來西亞藍金燈海 + 大氣藍邊光
- **■ AUDIO** ★"Think Big" 落點對全國發光(f3172)；格局最大
- **■ EDIT** 接 7.09
- **■ ASSETS** earth_malaysia(含東馬) · atmosphere_glow · cloud
- **■ NOTE** 「遍佈全馬」終極畫面;東馬不可漏(公司遍佈全馬的完整性)

---

## SHOT 7.09 — 推向東馬燈點 (Push to East Malaysia)
- **■ TC** f3192–3228 ｜ 133.0–134.5s ｜ Dur 36f ｜ WS ｜ 太空 ｜ 推
- **■ ACTION** 鏡頭推近東馬(沙巴/砂拉越)燈點、確認全國覆蓋;〔環境〕燈點仍在增亮
- **■ COLOR** 藍金燈海
- **■ AUDIO** 大副歌;EDIT 接 7.10(俯衝回地面)
- **■ ASSETS** earth_malaysia
- **■ NOTE** 強調「全馬」非僅西馬;品牌完整性

---

## SHOT 7.10 — 俯衝回人群 (Dive Back In)
- **■ TC** f3228–3276 ｜ 134.5–136.5s ｜ Dur 48f ｜ WS→MS ｜ 24mm ｜ dive-in
- **■ ACTION** f3228–3258〔主〕鏡頭從太空高速俯衝穿雲回到地面廣場(速度感、雲撕裂);f3258–3276〔主〕減速穩定於人群上方
- **■ FX** 高速俯衝 + 穿雲 + 速度線
- **■ COLOR** 太空→燈海
- **■ AUDIO** "we make the path for the future we trust";EDIT 接 7.11
- **■ ASSETS** cloud · crowd
- **■ NOTE** 把宏大收回到「人」;dive-in 是技術亮點鏡

---

## SHOT 7.11 — 六人站人群中央 (The Six · Center)
- **■ TC** f3276–3324 ｜ 136.5–138.5s ｜ Dur 48f ｜ MS ｜ 40mm ｜ T2.8 ｜ 環繞
- **■ STAGING** 四位老闆(Marcus/Evon/Steve/Yuki) + 阿凱 + 阿俊 並肩站廣場正中央,人群環繞;此處老闆**正式露臉群像**(呼應 SEQ01 起點)
- **■ ACTION**〔主〕六人並肩舉燈/握拳;人群環繞歡呼揮燈;〔次〕衣物旗幟動;〔環境〕藍金光自中心擴散
- **■ FACE** 六人各自神態(老闆自豪、阿凱昂揚、阿俊溫暖)
- **■ FX** crowd 環繞 + 中心光擴散
- **■ LIGHT** 藍金燈海環繞,六人被中心光提亮
- **■ COLOR** 藍金
- **■ AUDIO** 大副歌;EDIT 接 7.12–7.14 三顆 CU
- **■ ASSETS** marcus/evon/steve/yuki_rig(露臉・需簽核) · kai_rig · jun_rig · crowd_2000
- **■ NOTE** ⚠️ 四老闆此鏡露臉,肖像精度最高、必簽核;六人同框＝起點與今天的合一

---

## SHOT 7.12 — 阿凱昂揚 (Kai · CU)
- **■ TC** f3324–3360 ｜ 138.5–140.0s ｜ Dur 36f ｜ CU ｜ 85mm ｜ T2.0
- **■ ACTION** 阿凱(階段3)舉燈、昂首、藍火最盛、張口同唱;〔微〕眼中映燈海
- **■ FACE** 自信、熱血、眼有光
- **■ COLOR** 藍金 + 藍火
- **■ AUDIO** 副歌;EDIT 接 7.13
- **■ ASSETS** kai_rig(階段3)
- **■ NOTE** 藍火達全片最強

---

## SHOT 7.13 — 阿俊熱淚 (Jun · CU)
- **■ TC** f3360–3396 ｜ 140.0–141.5s ｜ Dur 36f ｜ CU ｜ 85mm ｜ T2.0
- **■ ACTION** 阿俊(階段3)望著滿場團隊、熱淚盈眶又笑、暖光最盛;〔微〕淚光、嘴角顫
- **■ FACE** 溫暖、感動、與有榮焉
- **■ COLOR** 藍金 + 暖光
- **■ AUDIO** 副歌;EDIT 接 7.14
- **■ ASSETS** jun_rig(階段3) · tear_FX
- **■ NOTE** 暖光達全片最強;與阿凱對位收束

---

## SHOT 7.14 — 四老闆群像自豪 (Founders · Proud)
- **■ TC** f3396–3432 ｜ 141.5–143.0s ｜ Dur 36f ｜ MS ｜ 50mm ｜ T2.5
- **■ ACTION** 四位老闆並肩、欣慰自豪望向團隊與遠方;〔次〕衣物微動、彼此交換一個眼神;〔環境〕被燈海環繞
- **■ FACE** 四人各自神態:Marcus 遠光、Evon 溫定、Steve 有力、Yuki 親和
- **■ COLOR** 品牌藍 + 藍金燈海
- **■ AUDIO** 副歌;EDIT 接 7.15
- **■ ASSETS** four_founder_rigs(露臉・簽核)
- **■ NOTE** ⚠️ 肖像簽核;與 SEQ01 火種四人剪影呼應(從剪影到露臉=從起源到今天)

---

## SHOT 7.15 — 全場舉燈 (Crowd Raises Lights)
- **■ TC** f3432–3456 ｜ 143.0–144.0s ｜ Dur 24f ｜ WS ｜ 28mm ｜ 微升
- **■ ACTION** 全場 2000 人同時把燈高舉、燈海整片上揚;〔環境〕光更盛
- **■ FX** crowd 同步舉燈 + 燈海上揚
- **■ COLOR** 藍金燈海最盛
- **■ AUDIO** ★"Turning the thousands to millions for us!";EDIT 接 7.16
- **■ ASSETS** crowd_2000 · lantern_FX
- **■ NOTE** 集體動作,方便現場觀眾跟做

---

## SHOT 7.16 — 燈光向上匯聚 (Lights Converge → 轉場)
- **■ TC** f3456–3480 ｜ 144.0–145.0s ｜ Dur 24f ｜ WS ｜ 24mm ｜ 升
- **■ ACTION** f3456–3480〔主〕所有燈光開始向中心上方匯聚、向上凝結;鏡頭隨之上升;〔環境〕燈海如被吸向天空一點
- **■ FX** 燈海螺旋匯聚上升
- **■ COLOR** 藍金向上收束
- **■ AUDIO** 大副歌收尾;EDIT **轉場 SEQ08**(燈海匯聚 → 北極星成形)
- **■ ASSETS** lantern_FX · crowd
- **■ NOTE** 把「燈海」收束成「一顆星」,直接接 outro 北極星

---

## SEQ07 交付檢查
- [ ] ★f2808 穿雲卡 1:57 大副歌落點,誤差 ≤2 幀
- [ ] crowd 2000 人 LOD:遠景 impostor/粒子、近景 hero 精修,無複製感
- [ ] 7.08 全馬地圖含東馬,品牌完整性
- [ ] 7.11/7.14 四老闆露臉群像,肖像最高精度 + 必簽核
- [ ] 阿凱藍火/阿俊暖光此段達全片最強(連戲頂點)
- [ ] 7.16 燈海匯聚順接 SEQ08 北極星
