# CLAUDE.md — PropNex《Sharpen the Wing》動畫 MV 專案交接

> 本檔供 Claude Code（本機或任何新 session）啟動時自動載入，快速接上專案全局。
> 若你是接手的 Claude：先讀本檔 → 再讀 `mv-production/README.md` → 進行中的工作在 `mv-production/shooting-script/`。

## 專案一句話
為 **PropNex Malaysia** 主題曲 **《Sharpen the Wing》(2:33 / 153s / ~143 BPM / 雙副歌)** 製作一支
**CG 3D 動畫 MV**，風格 **《Inside Out》鮮明角色 +《Soul》靈魂溫度**，對外用於培訓/年會/頒獎。

## 已鎖定的創意決定（不要擅自更改，需與用戶 Bowie 確認）
- **結構**：8 環節，各自獨立支線、串成一齣完整的劇；對應歌曲段落（見 `05_MUSIC_SYNC_MAP.md`）。
- **雙主角（皆男性，虛構代言角色，佔位名可替換）**：
  - **阿凱 Kai**：精進的火，帶團隊+瘋狂自我精進+緊跟老闆培訓。招牌色藍 `#0070E0`，胸口「藍色學習之火」。
  - **阿俊 Jun**：溫暖的光，好大哥/暖男/關懷 agent。招牌色琥珀 `#E9A23B`，胸口「琥珀暖暈」。
- **四位老闆（真名・真人・全片穿插引路人，對外片需肖像授權簽核）**：
  Marcus Teng (CEO) / Evon Heng (Executive Director) / Steve Tong / Yuki Wan。
- **公司事實**：PropNex 2018 進馬來西亞（恰好 8 年）；67→2000 人、遍佈全馬；
  願景 To Be Market Leader（靠培訓與人才發展）；信條 Good to Great · Think Big · Thousands to Millions · 4E。
- **母題符號**：一束光 / 光鳥 (Sharpen the Wing 振翅) / 藍金燈海 / 北極星(market leader)。
- **品牌色**：navy `#0A2540`、blue `#0070E0`、sky `#00AEEF`、amber `#E9A23B`、gold `#FFF4D6`、doubt-grey `#566370`。
- **色彩弧線**：灰冷質疑 → 藍色精進 → 藍金交融 → 暖金家園。
- **兩個幀級最強卡點**：副歌1落點 **0:44**（雲開神光）、大副歌落點 **1:57**（穿雲燈海）。
- **技術規格**：24fps 交付（hero/慢動作以 48–120fps 算再 retime）、16:9、4K、Pixar/Soul 級 CG 細緻度（見 `08_CG_DETAIL_REFERENCE.md`）。

## 歌曲（用戶提供，未進 repo）
檔名 `Sharpen_the_Wing.mp3`，153.42s。完整歌詞與逐段對位見 `05_MUSIC_SYNC_MAP.md`。歌曲尚無逐字 timecode（需在 DAW 用波形鎖定）。

## 檔案地圖
```
mv-production/
  README.md                     總導覽
  00_PRODUCTION_BIBLE.md         聖經總綱
  01_STORY_SCRIPT.md             分場劇本 + 鏡頭表（beat 級）
  02_CHARACTER_DESIGN.md         角色設定 / model sheet
  03_ART_DIRECTION_COLORSCRIPT.md 美術 + 色彩劇本
  04_CG_PIPELINE.md              13 工序製作管線
  05_MUSIC_SYNC_MAP.md           完整歌詞 × 畫面對位
  06_SCHEDULE_BUDGET_TEAM.md     排程/團隊/預算
  07_AI_ASSISTED_PRODUCTION.md   AI 輔助路線
  08_CG_DETAIL_REFERENCE.md      CG 細緻度全參照（120fps 等）
  09_PROMPT_BIBLE.md             八維度 prompt（美術/編導/場景/鏡頭/動作/表情/情緒/調色）
  pitch/index.html               提案級互動 HTML（exec summary）
  shooting-script/               ★ 製作級・逐幀拍攝腳本（CG designer 直接照做）
    00_STANDARD_AND_SHOTLIST.md  製作標準 + 全片 ~90 顆鏡頭母表（含時間碼）
    SEQ01_火種.md ... SEQ08_願景.md  逐鏡逐幀分解
```

## 目前進度（更新於本次 session）
- [x] 00–09 製作文件 + 提案 HTML 完成
- [x] 製作級拍攝腳本：標準 + 全片鏡頭母表、SEQ01、SEQ02 完成（逐幀）
- [ ] **進行中**：SEQ03–SEQ08 逐幀分解（用 SEQ01/02 的同一格式補完）
- [ ] 待用戶提供：四老闆官方多角度照+授權、leader 真名/形象、Logo 向量檔、歌曲逐字 timecode

## 待辦/下一步（給接手的 Claude）
1. 依 `shooting-script/00_STANDARD_AND_SHOTLIST.md` 的母表，逐一把 SEQ03–08 寫到 SEQ01/02 的深度。
2. 完成後可選：把 shooting-script 生成一個 HTML 檢視器（比 pitch/ 更細）。
3. 任何牽涉真人老闆形象、品牌合規、預算的決定，先問用戶 Bowie。

## 工作慣例
- 開發分支：`claude/company-theme-song-mv-fe9z8k`。commit 後 `git push -u origin <branch>`。
- 文件用繁體中文；技術名詞中英並用。
- 不要把這串雲端對話當記憶——一切「決定」以本檔 + repo 文件為準。
