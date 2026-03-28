# PPTX Execution Guide — Complete Runtime Instructions

## 环境要求

```bash
# 检查 Node.js 版本（需要 ≥ 16）
node -v

# 如果没有 Node.js，先安装：
# macOS: brew install node
# 或去 https://nodejs.org 下载安装包
```

## 项目初始化（一次性）

```bash
mkdir my-presentation && cd my-presentation
npm init -y
npm install pptxgenjs
```

目录结构：
```
my-presentation/
  package.json
  slide.js          ← 你的生成脚本
  assets/           ← 图片、GIF 资源
  output/           ← 输出 PPTX 目录
```

## 运行方式

```bash
node slide.js
# 输出：output/presentation.pptx
# 用 PowerPoint 或 Keynote 打开即可编辑
```

---

## 品牌颜色常量（唯一权威来源）

```javascript
// 所有脚本必须从这里引用颜色，不得硬编码其他值
const COLORS = {
  ORANGE : 'E87722',  // 主色：标题、重点边框、KPI数字
  TEAL   : '009999',  // 副色：辅助标题、信息卡头部、英文副标题
  BLACK  : '1a1a1a',  // 正文文字
  GRAY   : '888888',  // 标签文字、caption
  LGRAY  : 'F5F5F5',  // 卡片背景、表格交替行
  WHITE  : 'FFFFFF',  // 幻灯片背景、白色文字
};
```

---

## 完整示范脚本：Feature Demo Slide（左解释 / 右证明）

这是最常用的 Slide 格式，可作为所有功能页的基础模板。

```javascript
const PptxGenJS = require('pptxgenjs');

const COLORS = {
  ORANGE: 'E87722', TEAL: '009999', BLACK: '1a1a1a',
  GRAY: '888888',   LGRAY: 'F5F5F5', WHITE: 'FFFFFF',
};

const pres = new PptxGenJS();
pres.layout = 'LAYOUT_WIDE'; // 13.33" × 7.5"

// ─────────────────────────────────────────────
// SLIDE: Feature Demo（模板参考 R·Agent Slide 6-8）
// ─────────────────────────────────────────────
const slide = pres.addSlide();

// 1. 页面标题
slide.addText('AI 智能比对分析', {
  x: 0.5, y: 0.22, w: 11.0, h: 0.55,
  fontSize: 36, bold: true, color: COLORS.ORANGE,
  fontFace: 'Arial',
});

// 2. 公司 Logo 占位（实际使用时替换为真实图片）
slide.addText('Siemens Healthineers', {
  x: 11.2, y: 0.2, w: 1.9, h: 0.4,
  fontSize: 10, color: COLORS.GRAY, align: 'right',
});

// ── 左栏 ─────────────────────────────────────
// 3. 左栏背景（轻灰，增强分区感）
slide.addShape(pres.ShapeType.rect, {
  x: 0.4, y: 0.9, w: 5.3, h: 6.3,
  fill: { color: COLORS.LGRAY }, line: { color: COLORS.LGRAY },
});

// 4. Section Header: Chapter Scope
slide.addText('Chapter Scope', {
  x: 0.55, y: 0.98, w: 5.0, h: 0.35,
  fontSize: 18, bold: true, color: COLORS.BLACK,
});
slide.addText('Chapters 1–3  |  Coverage: 10%', {
  x: 0.55, y: 1.36, w: 4.8, h: 0.28,
  fontSize: 12, color: COLORS.GRAY,
});

// 5. Section Header: Technical Challenges
slide.addText('Technical Challenges', {
  x: 0.55, y: 1.82, w: 5.0, h: 0.35,
  fontSize: 18, bold: true, color: COLORS.BLACK,
});

// Challenge 盒子（白底 + 橙色边框）
const challenges = ['格式不统一', '专业术语歧义', '版本管控缺失'];
challenges.forEach((text, i) => {
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.55 + i * 1.68, y: 2.2, w: 1.55, h: 0.6,
    rectRadius: 0.06,
    fill: { color: COLORS.WHITE },
    line: { color: COLORS.ORANGE, width: 2 },
  });
  slide.addText(text, {
    x: 0.55 + i * 1.68, y: 2.2, w: 1.55, h: 0.6,
    fontSize: 12, color: COLORS.BLACK, align: 'center', valign: 'middle',
  });
});

// 6. Section Header: Process Flow
slide.addText('Process Flow', {
  x: 0.55, y: 3.0, w: 5.0, h: 0.35,
  fontSize: 18, bold: true, color: COLORS.BLACK,
});

// 步骤圆圈（4步）
const steps = ['Upload', 'Parse', 'Compare', 'Export'];
steps.forEach((label, i) => {
  const cx = 0.75 + i * 1.2;
  // 圆形
  slide.addShape(pres.ShapeType.ellipse, {
    x: cx, y: 3.42, w: 0.55, h: 0.55,
    fill: { color: COLORS.ORANGE }, line: { color: COLORS.ORANGE },
  });
  // 步骤编号
  slide.addText(`0${i + 1}`, {
    x: cx, y: 3.42, w: 0.55, h: 0.55,
    fontSize: 14, bold: true, color: COLORS.WHITE,
    align: 'center', valign: 'middle',
  });
  // 步骤标签
  slide.addText(label, {
    x: cx - 0.1, y: 4.02, w: 0.75, h: 0.28,
    fontSize: 12, color: COLORS.BLACK, align: 'center',
  });
  // 箭头（最后一步不加）
  if (i < 3) {
    slide.addText('→', {
      x: cx + 0.55, y: 3.49, w: 0.5, h: 0.4,
      fontSize: 16, color: COLORS.GRAY, align: 'center',
    });
  }
});

// 7. Section Header: Quality Gate
slide.addText('Quality Gate', {
  x: 0.55, y: 4.5, w: 5.0, h: 0.35,
  fontSize: 18, bold: true, color: COLORS.BLACK,
});

// KPI 指标（3个）
const kpis = [
  { num: '>95%', label: 'Accuracy' },
  { num: '<3s',  label: 'Speed' },
  { num: '✓',    label: 'Audit Trail' },
];
kpis.forEach((kpi, i) => {
  const kx = 0.6 + i * 1.7;
  slide.addText(kpi.num, {
    x: kx, y: 4.9, w: 1.5, h: 0.55,
    fontSize: 30, bold: true, color: COLORS.ORANGE,
    align: 'center',
  });
  slide.addText(kpi.label, {
    x: kx, y: 5.48, w: 1.5, h: 0.3,
    fontSize: 12, color: COLORS.GRAY, align: 'center',
  });
});

// ── 右栏 ─────────────────────────────────────
// 8. 右栏标题
slide.addText('AI Output — Real Document', {
  x: 6.0, y: 0.98, w: 6.8, h: 0.35,
  fontSize: 16, bold: true, color: COLORS.TEAL,
});

// 9. 证据区域（表格示例：AI 比对结果）
const tableData = [
  [
    { text: '条款编号', options: { bold: true, color: COLORS.WHITE, fill: COLORS.ORANGE } },
    { text: '原始内容', options: { bold: true, color: COLORS.WHITE, fill: COLORS.ORANGE } },
    { text: 'AI 识别',  options: { bold: true, color: COLORS.WHITE, fill: COLORS.ORANGE } },
    { text: '状态',     options: { bold: true, color: COLORS.WHITE, fill: COLORS.ORANGE } },
  ],
  ['1.2.3', '产品有效期不少于24个月', '有效期：24个月', { text: '✓ 一致', options: { color: '4CAF50' } }],
  ['2.1.1', '检测灵敏度≥99%',         '灵敏度：98.5%',   { text: '⚠ 偏差', options: { color: 'E53935' } }],
  ['3.4.2', '说明书须含禁忌症说明',    '包含禁忌症章节',  { text: '✓ 一致', options: { color: '4CAF50' } }],
];
slide.addTable(tableData, {
  x: 6.0, y: 1.4, w: 6.8, h: 2.4,
  colW: [1.2, 2.3, 2.3, 1.0],
  border: { pt: 0.5, color: 'DDDDDD' },
  fontSize: 12,
  fontFace: 'Arial',
  rowH: 0.5,
});

// 10. 底部差异说明卡（白底+橙色左边框）
slide.addShape(pres.ShapeType.rect, {
  x: 6.0, y: 4.0, w: 6.8, h: 2.8,
  fill: { color: COLORS.WHITE }, line: { color: 'DDDDDD', width: 1 },
});
slide.addShape(pres.ShapeType.rect, {
  x: 6.0, y: 4.0, w: 0.06, h: 2.8,
  fill: { color: COLORS.ORANGE }, line: { color: COLORS.ORANGE },
});
slide.addText('差异详情 — 条款 2.1.1', {
  x: 6.15, y: 4.08, w: 6.5, h: 0.35,
  fontSize: 14, bold: true, color: COLORS.BLACK,
});
slide.addText([
  { text: '要求值：', options: { bold: true } },
  { text: '灵敏度 ≥ 99%\n' },
  { text: '实测值：', options: { bold: true, color: COLORS.ORANGE } },
  { text: '灵敏度 98.5%，差值 0.5%\n' },
  { text: '建议：', options: { bold: true } },
  { text: '重新验证第3批次数据，补充置信区间说明' },
], {
  x: 6.15, y: 4.48, w: 6.5, h: 2.2,
  fontSize: 12, color: COLORS.BLACK,
  bullet: false,
});

// 11. 页码
slide.addText('6', {
  x: 12.6, y: 7.1, w: 0.5, h: 0.28,
  fontSize: 12, color: COLORS.GRAY, align: 'right',
});

// 12. Speaker Notes（演讲稿）
slide.addNotes(`
这一页展示的是 AI 智能比对分析的核心能力。
左侧说明我们的处理范围是第1到第3章节，约占全文档的10%。
三个主要技术挑战是：格式不统一、专业术语歧义、版本管控缺失。
右侧是真实文档的比对结果——系统自动识别出第2.1.1条存在偏差。
这个功能让审核人员不需要逐行手工比对，节省了大约70%的时间。
`);

// ─────────────────────────────────────────────
// 输出文件
// ─────────────────────────────────────────────
pres.writeFile({ fileName: 'output/presentation.pptx' })
  .then(() => console.log('✅ PPTX generated: output/presentation.pptx'))
  .catch(err => console.error('❌ Error:', err));
```

---

## 常用模式速查

### addText 完整参数

```javascript
slide.addText('内容', {
  x: 0.5, y: 1.0,        // 位置（英寸）
  w: 5.0, h: 0.5,        // 尺寸（英寸）
  fontSize: 14,           // 字号（pt）
  bold: true,             // 加粗
  italic: false,
  color: 'E87722',        // 颜色（不含#）
  fontFace: 'Arial',      // 字体
  align: 'left',          // left / center / right
  valign: 'top',          // top / middle / bottom
  wrap: true,             // 自动换行
});
```

### addShape 常用形状

```javascript
// 矩形
slide.addShape(pres.ShapeType.rect, { x, y, w, h, fill: { color }, line: { color, width } });

// 圆角矩形（rectRadius 以英寸为单位）
slide.addShape(pres.ShapeType.roundRect, { x, y, w, h, rectRadius: 0.06, fill: ... });

// 椭圆（正圆时 w === h）
slide.addShape(pres.ShapeType.ellipse, { x, y, w, h, fill: ... });

// 直线
slide.addShape(pres.ShapeType.line, { x, y, w, h, line: { color, width } });
```

### addChart 原生图表

```javascript
slide.addChart(pres.ChartType.bar, [
  { name: '完成率', labels: ['Q1','Q2','Q3','Q4'], values: [65, 72, 80, 85] },
], {
  x: 0.5, y: 1.5, w: 5.5, h: 4.0,
  barDir: 'col',                          // 竖柱
  chartColors: ['E87722', '009999'],
  showLegend: true, legendPos: 'b',
  showValue: true,
  dataLabelFontSize: 11,
  catAxisLabelFontSize: 12,
  valAxisLabelFontSize: 12,
});
```

### addTable 规范

```javascript
slide.addTable(rows, {
  x: 0.5, y: 1.0, w: 12.0, h: 4.0,
  colW: [2.0, 4.0, 4.0, 2.0],    // 各列宽，总和 = w
  rowH: 0.45,                      // 行高
  border: { pt: 0.5, color: 'DDDDDD' },
  fontSize: 12,
  fontFace: 'Arial',
});
// 表头行：fill: COLORS.ORANGE, color: COLORS.WHITE, bold: true
// 数据行：fill: COLORS.WHITE 或 COLORS.LGRAY（交替）
```

---

## 常见错误处理

| 错误信息 | 原因 | 解决 |
|---------|------|------|
| `Cannot find module 'pptxgenjs'` | 没有安装依赖 | `npm install pptxgenjs` |
| `ENOENT: no such file or directory, open 'output/...'` | output 目录不存在 | `mkdir -p output` |
| 字体显示不对 | 系统没有指定字体 | 改为 `Arial` 或 `Calibri`（通用字体） |
| 颜色不对 | 颜色值带了 `#` 号 | pptxgenjs 颜色值不加 `#`，直接写 `E87722` |
| 表格列宽加起来不等于 w | colW 数组之和 ≠ w | 检查 colW 之和 === `w` 参数 |
