# LoRA 资源与获取指南

## 方式一：直接使用 CivitAI LoRA（最快）

### 搜索入口
- https://civitai.com/models?tag=persona+5
- https://civitai.com/models?tag=cel+shading&types=LORA

### 使用方式

CivitAI 的 LoRA 下载链接可以直接传给 fal.ai：

```javascript
// 方式：先下载到本地，再上传到 fal storage
// 或使用 fal 支持的直接 URL（需验证 CivitAI 链接可直接访问）

const result = await fal.subscribe("fal-ai/flux-lora/image-to-image", {
  input: {
    loras: [{
      path: "https://civitai.com/api/download/models/XXXXX",  // 替换为实际 model ID
      scale: 0.85
    }]
  }
});
```

> **注意**：CivitAI 部分模型需要登录 API Key 才能下载。
> 替代方案：先下载到本地，上传到 fal storage，使用 fal 的 storage URL。

### 上传到 fal storage

```javascript
import { fal } from "@fal-ai/client";

// 上传本地 LoRA 文件
const file = new File([loraBuffer], "style.safetensors");
const url = await fal.storage.upload(file);
console.log("LoRA URL:", url);
// 然后在 loras 参数中使用这个 URL
```

---

## 方式二：HuggingFace 上的免费 LoRA

直接引用 HuggingFace 上的 FLUX 兼容 LoRA：

```javascript
loras: [{
  path: "https://huggingface.co/YOUR_USERNAME/LORA_REPO/resolve/main/lora.safetensors",
  scale: 0.8
}]
```

### 推荐 HuggingFace 搜索
- https://huggingface.co/models?search=persona+5+flux
- https://huggingface.co/models?search=cel+shade+lora+flux

---

## 方式三：自训练 LoRA（最高质量，$2 一次）

适用场景：想要完全精准的某一种独特风格。

### 训练数据准备

1. 收集 10-30 张目标风格的参考图（越多越好）
2. 分辨率建议 1024x1024 以上
3. 图像要风格统一，无压缩噪点
4. 打包为 ZIP 文件

**P5 风格训练素材来源：**
- 游戏截图（官方宣传图质量最高）
- 官方艺术画集扫描
- Atlus 官方 Twitter/网站发布的宣传图

### 训练调用

```javascript
const training = await fal.subscribe("fal-ai/flux-lora-fast-training", {
  input: {
    images_data_url: "YOUR_ZIP_URL",      // 上传到 fal storage 的 ZIP
    trigger_word: "p5style painting",      // 唯一触发词
    is_style: true,                        // 风格训练模式
    steps: 1500,                           // 推荐 1000-2000 步
  }
});

console.log("LoRA URL:", training.diffusers_lora_file.url);
// 保存这个 URL 供后续使用
```

### 训练参数建议

| 参数 | 推荐值 | 说明 |
|------|--------|------|
| steps | 1500 | P5 风格高度特化，需要充分训练 |
| is_style | true | 禁用自动字幕，避免干扰风格捕获 |
| trigger_word | `p5s illustration` | 唯一 token + 类别描述 |

---

## 验证 LoRA 效果

训练完成后，用这个 Prompt 测试：

```
p5s illustration of a coffee shop interior,
[然后不加其他风格词，看 LoRA 自己是否能驱动风格]
```

如果风格不够强，适当提高 `scale` 到 0.9-1.0；
如果创意受限（只能生成 P5 场景），降低 `scale` 到 0.6-0.7。
