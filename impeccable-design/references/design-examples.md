# 设计示例和代码片段

## 排版示例

### 字体比例系统
```css
/* 基于 1.25 比例的字体大小 */
:root {
  --font-size-xs: 0.8rem;    /* 12.8px */
  --font-size-sm: 1rem;      /* 16px */
  --font-size-base: 1.25rem; /* 20px */
  --font-size-lg: 1.563rem;  /* 25px */
  --font-size-xl: 1.953rem;  /* 31.25px */
  --font-size-2xl: 2.441rem; /* 39.06px */
}

/* 行高设置 */
:root {
  --line-height-tight: 1.2;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
}
```

### 标题层次
```html
<h1 class="text-4xl font-bold leading-tight">主要标题</h1>
<h2 class="text-3xl font-semibold leading-snug">次要标题</h2>
<h3 class="text-2xl font-medium leading-normal">三级标题</h3>
<h4 class="text-xl font-medium leading-normal">四级标题</h4>
<p class="text-base leading-relaxed">正文内容，使用合适的行高确保可读性。</p>
```

## 色彩系统示例

### CSS 自定义属性
```css
/* 主色调 */
:root {
  --color-primary-50: #eff6ff;
  --color-primary-100: #dbeafe;
  --color-primary-200: #bfdbfe;
  --color-primary-300: #93c5fd;
  --color-primary-400: #60a5fa;
  --color-primary-500: #3b82f6; /* 主色 */
  --color-primary-600: #2563eb;
  --color-primary-700: #1d4ed8;
  --color-primary-800: #1e40af;
  --color-primary-900: #1e3a8a;
}

/* 中性色 */
:root {
  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-200: #e5e7eb;
  --color-gray-300: #d1d5db;
  --color-gray-400: #9ca3af;
  --color-gray-500: #6b7280;
  --color-gray-600: #4b5563;
  --color-gray-700: #374151;
  --color-gray-800: #1f2937;
  --color-gray-900: #111827;
}

/* 语义色 */
:root {
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-error: #ef4444;
  --color-info: #3b82f6;
}
```

## 间距系统示例

### 基于 8px 的间距单位
```css
:root {
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-5: 1.25rem;  /* 20px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-10: 2.5rem;  /* 40px */
  --space-12: 3rem;    /* 48px */
  --space-16: 4rem;    /* 64px */
  --space-20: 5rem;    /* 80px */
  --space-24: 6rem;    /* 96px */
}
```

### 实用类示例
```css
/* 间距实用类 */
.m-4 { margin: var(--space-4); }
.p-4 { padding: var(--space-4); }
.gap-4 { gap: var(--space-4); }

/* 响应式间距 */
@media (min-width: 768px) {
  .md\:m-6 { margin: var(--space-6); }
  .md\:p-6 { padding: var(--space-6); }
}
```

## 交互组件示例

### 按钮组件
```html
<button class="btn btn-primary">
  主要按钮
</button>

<button class="btn btn-secondary" disabled>
  禁用按钮
</button>

<button class="btn btn-outline">
  轮廓按钮
</button>
```

```css
/* 按钮基础样式 */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--space-2) var(--space-4);
  border-radius: 0.375rem;
  font-weight: 500;
  font-size: var(--font-size-sm);
  line-height: var(--line-height-normal);
  transition: all 150ms ease-out;
  cursor: pointer;
  border: 1px solid transparent;
}

/* 按钮状态 */
.btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.btn:focus {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
}

.btn:active {
  transform: translateY(0);
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

/* 按钮变体 */
.btn-primary {
  background-color: var(--color-primary-500);
  color: white;
}

.btn-primary:hover {
  background-color: var(--color-primary-600);
}

.btn-secondary {
  background-color: var(--color-gray-200);
  color: var(--color-gray-800);
}

.btn-outline {
  background-color: transparent;
  border-color: var(--color-gray-300);
  color: var(--color-gray-700);
}

.btn-outline:hover {
  background-color: var(--color-gray-50);
}
```

### 卡片组件
```html
<div class="card">
  <div class="card-header">
    <h3 class="card-title">卡片标题</h3>
  </div>
  <div class="card-body">
    <p>卡片内容区域，可以包含各种内容。</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-primary">操作按钮</button>
  </div>
</div>
```

```css
/* 卡片样式 */
.card {
  background-color: white;
  border-radius: 0.5rem;
  border: 1px solid var(--color-gray-200);
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: box-shadow 150ms ease-out;
}

.card:hover {
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.card-header {
  padding: var(--space-4);
  border-bottom: 1px solid var(--color-gray-200);
}

.card-title {
  font-size: var(--font-size-lg);
  font-weight: 600;
  margin: 0;
}

.card-body {
  padding: var(--space-4);
}

.card-footer {
  padding: var(--space-4);
  border-top: 1px solid var(--color-gray-200);
  background-color: var(--color-gray-50);
}
```

## 响应式设计示例

### 移动优先的媒体查询
```css
/* 基础样式（移动端） */
.container {
  width: 100%;
  padding: 0 var(--space-4);
}

/* 平板设备 */
@media (min-width: 768px) {
  .container {
    max-width: 768px;
    margin: 0 auto;
    padding: 0 var(--space-6);
  }
}

/* 桌面设备 */
@media (min-width: 1024px) {
  .container {
    max-width: 1024px;
    padding: 0 var(--space-8);
  }
}

/* 大桌面设备 */
@media (min-width: 1280px) {
  .container {
    max-width: 1280px;
  }
}
```

### 响应式网格布局
```html
<div class="grid">
  <div class="col-12 md:col-6 lg:col-4">内容1</div>
  <div class="col-12 md:col-6 lg:col-4">内容2</div>
  <div class="col-12 md:col-6 lg:col-4">内容3</div>
</div>
```

```css
/* 网格系统 */
.grid {
  display: grid;
  gap: var(--space-4);
}

/* 移动端：单列 */
.col-12 {
  grid-column: span 12;
}

/* 平板：两列 */
@media (min-width: 768px) {
  .md\:col-6 {
    grid-column: span 6;
  }
}

/* 桌面：三列 */
@media (min-width: 1024px) {
  .lg\:col-4 {
    grid-column: span 4;
  }
}
```

## 动效示例

### CSS 过渡动画
```css
/* 淡入淡出 */
.fade-in {
  opacity: 0;
  animation: fadeIn 300ms ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* 滑动进入 */
.slide-in {
  transform: translateX(-100%);
  animation: slideIn 400ms cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

@keyframes slideIn {
  to {
    transform: translateX(0);
  }
}

/* 缩放效果 */
.scale-up {
  transform: scale(0.95);
  animation: scaleUp 200ms ease-out forwards;
}

@keyframes scaleUp {
  to {
    transform: scale(1);
  }
}
```

### 加载状态
```html
<div class="loading">
  <div class="loading-spinner"></div>
  <p class="loading-text">加载中...</p>
</div>
```

```css
/* 加载动画 */
.loading {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: var(--space-8);
}

.loading-spinner {
  width: 40px;
  height: 40px;
  border: 3px solid var(--color-gray-200);
  border-top-color: var(--color-primary-500);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.loading-text {
  margin-top: var(--space-4);
  color: var(--color-gray-600);
  font-size: var(--font-size-sm);
}
```

## 可访问性示例

### 屏幕阅读器友好
```html
<!-- 隐藏视觉但保留给屏幕阅读器 -->
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

<!-- 使用示例 -->
<button class="btn">
  <span class="sr-only">关闭菜单</span>
  <svg aria-hidden="true">...</svg>
</button>
```

### ARIA 属性
```html
<!-- 进度指示器 -->
<div 
  role="progressbar" 
  aria-valuenow="75" 
  aria-valuemin="0" 
  aria-valuemax="100"
  aria-label="任务完成进度"
>
  <div class="progress-bar" style="width: 75%"></div>
</div>

<!-- 模态对话框 -->
<div 
  role="dialog" 
  aria-modal="true" 
  aria-labelledby="dialog-title"
  aria-describedby="dialog-description"
>
  <h2 id="dialog-title">确认操作</h2>
  <p id="dialog-description">您确定要执行此操作吗？</p>
</div>
```

## 性能优化示例

### 图片优化
```html
<!-- 响应式图片 -->
<img
  src="image-400.jpg"
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 768px) 100vw, 50vw"
  alt="描述性文字"
  loading="lazy"
>

<!-- WebP 格式支持 -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="描述性文字">
</picture>
```

### CSS 优化
```css
/* 使用 CSS 变量减少重复 */
:root {
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

/* 减少重绘 */
.will-change-transform {
  will-change: transform;
}

/* 硬件加速 */
.hardware-accelerated {
  transform: translateZ(0);
}
```

## 设计模式示例

### 技术文档布局
```html
<article class="documentation">
  <header class="doc-header">
    <h1>API 参考文档</h1>
    <p class="doc-description">详细的 API 使用说明和示例。</p>
  </header>
  
  <div class="doc-content">
    <nav class="doc-sidebar">
      <!-- 导航菜单 -->
    </nav>
    
    <main class="doc-main">
      <section class="doc-section">
        <h2>快速开始</h2>
        <pre><code>npm install package-name</code></pre>
      </section>
    </main>
  </div>
</article>
```

### 仪表板布局
```html
<div class="dashboard">
  <header class="dashboard-header">
    <!-- 顶部导航 -->
  </header>
  
  <div class="dashboard-content">
    <aside class="dashboard-sidebar">
      <!-- 侧边栏菜单 -->
    </aside>
    
    <main class="dashboard-main">
      <div class="dashboard-grid">
        <div class="dashboard-card">卡片1</div>
        <div class="dashboard-card">卡片2</div>
        <div class="dashboard-card">卡片3</div>
      </div>
    </main>
  </div>
</div>
```

这些示例展示了 impeccable.style 设计原则的实际应用，可以作为创建高质量前端界面的参考。