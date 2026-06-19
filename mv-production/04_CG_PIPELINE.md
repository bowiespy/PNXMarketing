# 04｜CG 製作管線 (Full CG Production Pipeline)

> 比擬 Pixar / Universal(Illumination) 的工業級 CG 流程，落地成可執行的 13 道工序。
> 每道工序標明：**目的 / 交付物 (deliverable) / 工具 / 驗收門檻 (gate)**。
> 流程採「逐工序簽核 (review gate)」制——上一關沒過，不進下一關，避免返工。

---

## 階段總覽

```
DEVELOPMENT → PRE-PRODUCTION → PRODUCTION → POST-PRODUCTION
   開發            前期             製作            後期
   (1)         (2-5)            (6-12)           (13)
```

---

## ▍DEVELOPMENT 開發

### 工序 1｜故事 / 劇本 / Treatment
- **目的**：鎖定故事、主題、8 環節結構。
- **交付物**：本 repo 的 `00`–`03` 文件（聖經、劇本、角色、色彩）。
- **工具**：文件 + 參考片 moodboard。
- **驗收門檻 (Gate A)**：四位創辦人 + 兩位主角原型 leader 對「故事與情緒弧線」簽核。

---

## ▍PRE-PRODUCTION 前期

### 工序 2｜角色設計 & Model Sheet
- **目的**：定下所有角色的造型、表情、配色、比例。
- **交付物**：`02` 列出的 turnaround / expression sheet / color callout。
- **工具**：Photoshop / Procreate / Nomad Sculpt（概念）。
- **Gate B**：主角阿浩、凱琳三階段造型 + 兩盞燈設計通過。

### 工序 3｜視覺開發 Visual Development + Color Script
- **目的**：定美術風格、色彩劇本、光影聖經。
- **交付物**：`03` 的 8 張 color key + 全片色彩條 + lighting reference。
- **工具**：Photoshop / Blender 概念渲染 / Nuke (paint-over)。
- **Gate C**：整體 look & feel 過審（確認「Pixar 溫暖寫實卡通」方向）。

### 工序 4｜分鏡 Storyboard
- **目的**：把劇本 (`01`) 的鏡頭表畫成連續分鏡圖。
- **交付物**：約 **120–160 格分鏡**（2:33、8 段、平均每段 15–20 格），含運鏡箭頭與時間註記。
- **工具**：Storyboard Pro / Procreate / Krita。
- **Gate D**：敘事可讀、鏡頭邏輯通順、無冷場。

### 工序 5｜動態分鏡 Animatic（**鎖音樂、鎖時長**）
- **目的**：把分鏡剪上《Sharpen the Wing》音軌，鎖定每個鏡頭的精確秒數。
- **交付物**：153 秒 animatic 影片（分鏡圖 + 音樂 + 暫定字卡）。
- **工具**：Premiere / DaVinci Resolve / Toon Boom。
- **Gate E（關鍵里程碑）**：**全片時長與卡點鎖死**。此後鏡頭時長不再變動，
  下游所有 3D 工序以 animatic 為唯一時間真相 (single source of truth)。

> 💡 強烈建議：在 animatic 階段就把 `05_MUSIC_SYNC_MAP.md` 的卡點全部驗證一遍。
> 一旦進入 3D，改時間的成本是 animatic 階段的數十倍。

---

## ▍PRODUCTION 製作

### 工序 6｜Layout（攝影機 & 走位）
- **目的**：在 3D 空間裡架攝影機、放角色替身 (proxy)、定走位與鏡頭運動。
- **交付物**：每個鏡頭的 3D layout（低模 blocking + camera animation）。
- **工具**：Blender / Maya。
- **Gate F**：攝影機運動與 animatic 一致，空間關係正確。

### 工序 7｜建模 Modeling
- **目的**：建出最終角色、場景、道具的高模/中模。
- **交付物**：角色 mesh（含拓樸乾淨的 face loop）、場景、道具、燈具。
- **工具**：Blender / Maya / ZBrush（雕刻細節）。
- **資產清單**：主角×2（三階段）、新生代×3-5、base mesh×8-10（複製成 67 人/群眾）、
  燈具×2、燈塔、辦公室、街道、城市、地標（雙子塔等）、光之鳥。
- **Gate G**：拓樸可動畫、比例符合 model sheet。

### 工序 8｜綁定 Rigging
- **目的**：給角色裝骨架與表情控制。
- **交付物**：身體 rig（IK/FK 切換）、臉部 rig（FACS blendshape ≥30 組）、燈具發光控制。
- **工具**：Blender Rigify / Maya（advanced skeleton）。
- **Gate H**：極端表情/姿勢無破面、無穿插。

### 工序 9｜材質 Surfacing / Shading / Texturing
- **目的**：上色、貼圖、設定物理材質（含膚質 SSS）。
- **交付物**：PBR 材質球、UV、貼圖（albedo/roughness/normal/SSS）。
- **工具**：Substance Painter / Blender shading / Mari。
- **重點**：膚質次表面散射 (SSS) 是 Pixar 溫暖感的關鍵；燈具用 emission + bloom 友善材質。
- **Gate I**：材質在 color script 指定燈光下顏色正確。

### 工序 10｜動畫 Animation（+ 群眾 Crowd Sim）
- **目的**：讓角色演戲。這是全片靈魂工序，工時佔比最高。
- **交付物**：每鏡頭角色表演動畫；⑦段 2000 人燈海用群眾模擬。
- **工具**：Blender / Maya；群眾：Houdini Crowd / Blender geometry-nodes instancing / Golaem(高階)。
- **重點**：① 表演要有「重量與意圖」(weight & intent)；② 對嘴若有歌詞需 lip-sync；
  ③ 群眾用 agent + 隨機變化避免複製感。
- **Gate J**：表演通過導演 review（情緒到位、節奏卡音樂）。

### 工序 11｜特效 FX
- **目的**：雨、體積霧、神光、燈火粒子、燈海、雲層、光之鳥拖尾。
- **交付物**：各鏡頭 FX pass（可分層輸出）。
- **工具**：Houdini（首選）/ Blender (Mantaflow + geometry nodes)。
- **重點鏡頭**：③雨 + 濕反光、④god rays、⑥⑦光粒子接力與燈海、⑦空拍體積雲、⑧北極星 bloom。
- **Gate K**：FX 與角色動畫整合無違和、可控可重算。

### 工序 12｜燈光 & 算圖 Lighting & Rendering
- **目的**：依 color script (`03`) 打光、輸出多層 AOV 算圖。
- **交付物**：每鏡頭 render passes（beauty / diffuse / specular / SSS / volume / cryptomatte 等）。
- **工具**：Blender Cycles / RenderMan / Arnold / Redshift（GPU）。
- **重點**：全片唯一主動光源是「信念之燈」邏輯（見 `03` 第4節）；用體積光與 GI 暖反彈。
- **Gate L**：每鏡頭通過 lighting review，雜訊 (noise) 在可接受門檻內。

---

## ▍POST-PRODUCTION 後期

### 工序 13｜合成 → 調色 → 混音 → 成片
- **13a 合成 Compositing**：疊合所有 AOV/FX 層，加景深、bloom、輝光、片尾字卡光粒子。工具：Nuke / DaVinci Fusion / After Effects。
- **13b 剪輯 Editorial**：依鎖定的 animatic 把成片鏡頭組裝起來。工具：Premiere / DaVinci Resolve。
- **13c 調色 Color Grade**：套全片暖調 LUT，統一「日落感」（陰影偏冷、高光偏暖）。工具：DaVinci Resolve。
- **13d 音樂與混音 Sound Mix**：主題曲為主軸，補上環境音 (foley/SFX)——雨聲、人群、點燈「叮」聲、北極星升空 whoosh。確認對白/字卡與音樂卡點。工具：Pro Tools / Audition / Reaper。
- **13e 成片 Master**：輸出多版本（見下方交付規格）。
- **Gate M（最終驗收）**：四位創辦人 + 兩位主角 leader 終審；活動現場大屏試播。

---

## 交付規格 (Delivery Specs)

| 用途 | 規格 |
|------|------|
| 活動現場大屏 | 1920×1080 或 4K (3840×2160)、ProRes 422 HQ、25/30fps |
| 社群完整版 | 1080p H.264 MP4 |
| 社群直式短版 | 1080×1920（拆⑦⑦高潮段做 teaser） |
| 8 段獨立支線短片 | 每段 15–30s 可單獨發布（劇本已設計成可拆） |
| 母帶存檔 | 無壓縮/ProRes 4444 + 專案工程檔 |

---

## 技術堆疊建議 (Recommended Stack)

| 路線 | DCC | 算圖 | FX | 合成 | 剪輯/調色 |
|------|-----|------|----|----|-----------|
| A 工作室級 | Maya | RenderMan/Arnold | Houdini | Nuke | Resolve |
| B 獨立製作（推薦） | Blender | Cycles (GPU) | Blender/Houdini Indie | Fusion/AE | Resolve |
| C AI 輔助快速版 | Blender + AI | Cycles/AI render | 簡化 | AE | Resolve |（見 `07`）

---

## 工時佔比參考（純 CG 路線）

```
動畫 Animation        ████████████  ~30%
燈光算圖 Light/Render  ████████      ~20%
建模綁定 Model/Rig     ██████        ~15%
FX                    █████         ~12%
前期(分鏡/animatic)    ████          ~10%
材質 Surfacing         ███           ~8%
合成後期 Comp/Post     ██            ~5%
```

> 結論：**前期 (animatic) 鎖得越死，後面省得越多。** 別急著進 3D。
