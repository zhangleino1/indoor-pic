<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg viewBox="0 0 1000 600" xmlns="http://www.w3.org/2000/svg">
  <!-- 背景网格和边框 -->
  <rect x="20" y="20" width="960" height="560" fill="white" stroke="none"/>
  
  <!-- 左侧输入层 - Raw CSI Data -->
  <g id="input-layer">
    <rect x="95" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- 输入层神经元 - 黑色圆点 -->
    <circle cx="120" cy="170" r="6" fill="black"/>
    <circle cx="120" cy="190" r="6" fill="black"/>
    <circle cx="120" cy="210" r="6" fill="black"/>
    <circle cx="120" cy="230" r="6" fill="black"/>
    <circle cx="120" cy="250" r="6" fill="black"/>
    <circle cx="120" cy="270" r="6" fill="black"/>
    <circle cx="120" cy="290" r="6" fill="black"/>
    <circle cx="120" cy="310" r="6" fill="black"/>
    
    <!-- 输入标签 -->
    <text x="120" y="345" text-anchor="middle" font-family="Arial" font-size="12">u⁰</text>
    <text x="120" y="365" text-anchor="middle" font-family="Arial" font-size="12">90</text>
    
    <!-- Raw CSI Data标签和箭头 -->
    <text x="120" y="400" text-anchor="middle" font-family="Arial" font-size="12">Raw CSI Data</text>
    <text x="120" y="415" text-anchor="middle" font-family="Arial" font-size="10">[m*N, 90]</text>
    <path d="M120,385 L120,370" stroke="#3D9970" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
    
    <!-- m*N 标记 -->
    <text x="140" y="80" text-anchor="middle" font-family="Arial" font-size="14">m*N</text>
    <path d="M110,85 Q125,75 140,85" stroke="black" stroke-width="1.5" fill="none"/>
  </g>

  <!-- 权重连接和隐藏层 K1 (Layer 1 - 灰色) -->
  <g id="layer1">
    <text x="170" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W¹ᵤ</text>
    <!-- 连接线从输入到Layer 1 -->
    <path d="M145,170 L195,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M145,170 L195,190" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M145,170 L195,210" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <!-- 更多连接线 -->
    <path d="M145,310 L195,270" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M145,310 L195,290" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M145,310 L195,310" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- Layer 1 方框 -->
    <rect x="195" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- Layer 1 神经元 - 灰色圆点 -->
    <circle cx="220" cy="170" r="6" fill="#808080"/>
    <circle cx="220" cy="190" r="6" fill="#808080"/>
    <circle cx="220" cy="210" r="6" fill="#808080"/>
    <circle cx="220" cy="230" r="6" fill="#808080"/>
    <circle cx="220" cy="250" r="6" fill="#808080"/>
    <circle cx="220" cy="270" r="6" fill="#808080"/>
    <circle cx="220" cy="290" r="6" fill="#808080"/>
    <circle cx="220" cy="310" r="6" fill="#808080"/>
    
    <text x="220" y="345" text-anchor="middle" font-family="Arial" font-size="12">u¹</text>
    <text x="220" y="390" text-anchor="middle" font-family="Arial" font-size="12">K1</text>
  </g>

  <!-- 权重连接和隐藏层 K2 (Layer 2 - 黑色) -->
  <g id="layer2">
    <text x="270" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W²ᵤ</text>
    <!-- 连接线从Layer 1到Layer 2 -->
    <path d="M245,170 L295,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M245,170 L295,190" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M245,310 L295,290" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M245,310 L295,310" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- Layer 2 方框 -->
    <rect x="295" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- Layer 2 神经元 - 黑色圆点 -->
    <circle cx="320" cy="170" r="6" fill="black"/>
    <circle cx="320" cy="190" r="6" fill="black"/>
    <circle cx="320" cy="210" r="6" fill="black"/>
    <circle cx="320" cy="230" r="6" fill="black"/>
    <circle cx="320" cy="250" r="6" fill="black"/>
    <circle cx="320" cy="270" r="6" fill="black"/>
    <circle cx="320" cy="290" r="6" fill="black"/>
    <circle cx="320" cy="310" r="6" fill="black"/>
    
    <text x="320" y="345" text-anchor="middle" font-family="Arial" font-size="12">u²</text>
    <text x="320" y="390" text-anchor="middle" font-family="Arial" font-size="12">K2</text>
  </g>

  <!-- 权重连接和隐藏层 K3 (Layer 3 - 灰色) -->
  <g id="layer3">
    <text x="370" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W³ᵤ</text>
    <!-- 连接线从Layer 2到Layer 3 -->
    <path d="M345,170 L395,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M345,310 L395,310" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- Layer 3 方框 -->
    <rect x="395" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- Layer 3 神经元 - 灰色圆点 -->
    <circle cx="420" cy="170" r="6" fill="#808080"/>
    <circle cx="420" cy="190" r="6" fill="#808080"/>
    <circle cx="420" cy="210" r="6" fill="#808080"/>
    <circle cx="420" cy="230" r="6" fill="#808080"/>
    <circle cx="420" cy="250" r="6" fill="#808080"/>
    <circle cx="420" cy="270" r="6" fill="#808080"/>
    <circle cx="420" cy="290" r="6" fill="#808080"/>
    <circle cx="420" cy="310" r="6" fill="#808080"/>
    
    <text x="420" y="345" text-anchor="middle" font-family="Arial" font-size="12">u³</text>
    <text x="420" y="390" text-anchor="middle" font-family="Arial" font-size="12">K3</text>
  </g>

  <!-- 权重连接和瓶颈层 K4 -->
  <g id="bottleneck">
    <text x="470" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W⁴ᵤ</text>
    <!-- 连接线从Layer 3到瓶颈层 -->
    <path d="M445,170 L495,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M445,310 L495,240" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- 瓶颈层方框 -->
    <rect x="495" y="150" width="60" height="180" rx="10" ry="10" stroke="black" stroke-width="2" fill="white"/>
    
    <!-- 瓶颈层神经元 - 黄色圆圈 -->
    <circle cx="515" cy="170" r="6" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="535" cy="170" r="6" fill="yellow" stroke="black" stroke-width="1"/>
    <circle cx="515" cy="190" r="6" fill="yellow" stroke="black" stroke-width="1"/>
    <circle cx="535" cy="190" r="6" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="515" cy="210" r="6" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="535" cy="210" r="6" fill="yellow" stroke="black" stroke-width="1"/>
    <circle cx="515" cy="230" r="6" fill="yellow" stroke="black" stroke-width="1"/>
    <circle cx="535" cy="230" r="6" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="515" cy="250" r="6" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="535" cy="250" r="6" fill="yellow" stroke="black" stroke-width="1"/>
    
    <!-- 瓶颈层标签 -->
    <text x="525" y="345" text-anchor="middle" font-family="Arial" font-size="12">K4</text>
    <text x="480" cy="230" font-family="Arial" font-size="14" fill="#3D9970">u⁴</text>
    <path d="M478,230 L490,230" stroke="#3D9970" stroke-width="1.5" fill="none" marker-end="url(#arrowhead)"/>
    
    <!-- Best Features Extracted 标签和箭头 -->
    <text x="525" y="110" text-anchor="middle" font-family="Arial" font-size="12">Best Features Extracted</text>
    <path d="M525,125 L525,145" stroke="#3D9970" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  </g>

  <!-- One-Hot Labels 部分 -->
  <g id="one-hot-labels">
    <!-- One-Hot Labels 标题 -->
    <text x="525" y="410" text-anchor="middle" font-family="Arial" font-size="12">One-Hot Labels</text>
    
    <!-- 标签矩阵 -->
    <rect x="495" y="420" width="60" height="80" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    
    <!-- 矩阵内部点 -->
    <circle cx="505" cy="430" r="5" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="525" cy="430" r="5" fill="black"/>
    <circle cx="545" cy="430" r="5" fill="white" stroke="black" stroke-width="1"/>
    
    <circle cx="505" cy="450" r="5" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="525" cy="450" r="5" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="545" cy="450" r="5" fill="white" stroke="black" stroke-width="1"/>
    
    <!-- 省略号 -->
    <text x="525" cy="470" text-anchor="middle" font-family="Arial" font-size="16">⋮ … ⋮</text>
    
    <circle cx="505" cy="490" r="5" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="525" cy="490" r="5" fill="white" stroke="black" stroke-width="1"/>
    <circle cx="545" cy="490" r="5" fill="black"/>
    
    <!-- 标签信息 -->
    <text x="470" cy="430" text-anchor="end" font-family="Arial" font-size="12" fill="#6A5ACD">labelⱼ</text>
    <path d="M475,430 L495,430" stroke="#6A5ACD" stroke-width="1.5" fill="none" marker-end="url(#arrowhead)"/>
    
    <text x="525" y="515" text-anchor="middle" font-family="Arial" font-size="12">K4 + N</text>
    <text x="425" y="475" text-anchor="middle" font-family="Arial" font-size="14" fill="#6A5ACD">v⁴ = u⁴</text>
    
    <!-- Labeled Vectors标签和箭头 -->
    <text x="525" y="550" text-anchor="middle" font-family="Arial" font-size="12">Labeled Vectors</text>
    <path d="M525,510 L525,535" stroke="#3D9970" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  </g>

  <!-- 右侧解码器部分 -->
  <!-- 权重连接和隐藏层 K3' -->
  <g id="decoder-layer3">
    <text x="570" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W³ᵥ</text>
    <!-- 连接线从瓶颈层到Layer 3' -->
    <path d="M555,170 L605,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M555,250 L605,310" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- Layer 3' 方框 -->
    <rect x="605" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- Layer 3' 神经元 - 灰色圆点 -->
    <circle cx="630" cy="170" r="6" fill="#808080"/>
    <circle cx="630" cy="190" r="6" fill="#808080"/>
    <circle cx="630" cy="210" r="6" fill="#808080"/>
    <circle cx="630" cy="230" r="6" fill="#808080"/>
    <circle cx="630" cy="250" r="6" fill="#808080"/>
    <circle cx="630" cy="270" r="6" fill="#808080"/>
    <circle cx="630" cy="290" r="6" fill="#808080"/>
    <circle cx="630" cy="310" r="6" fill="#808080"/>
    
    <text x="630" y="345" text-anchor="middle" font-family="Arial" font-size="12">v³</text>
    <text x="630" y="390" text-anchor="middle" font-family="Arial" font-size="12">K3</text>
  </g>

  <!-- 权重连接和隐藏层 K2' -->
  <g id="decoder-layer2">
    <text x="670" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W²ᵥ</text>
    <!-- 连接线从Layer 3'到Layer 2' -->
    <path d="M655,170 L705,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M655,310 L705,310" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- Layer 2' 方框 -->
    <rect x="705" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- Layer 2' 神经元 - 黑色圆点 -->
    <circle cx="730" cy="170" r="6" fill="black"/>
    <circle cx="730" cy="190" r="6" fill="black"/>
    <circle cx="730" cy="210" r="6" fill="black"/>
    <circle cx="730" cy="230" r="6" fill="black"/>
    <circle cx="730" cy="250" r="6" fill="black"/>
    <circle cx="730" cy="270" r="6" fill="black"/>
    <circle cx="730" cy="290" r="6" fill="black"/>
    <circle cx="730" cy="310" r="6" fill="black"/>
    
    <text x="730" y="345" text-anchor="middle" font-family="Arial" font-size="12">v²</text>
    <text x="730" y="390" text-anchor="middle" font-family="Arial" font-size="12">K2</text>
  </g>

  <!-- 权重连接和隐藏层 K1' -->
  <g id="decoder-layer1">
    <text x="770" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W¹ᵥ</text>
    <!-- 连接线从Layer 2'到Layer 1' -->
    <path d="M755,170 L805,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M755,170 L805,190" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M755,310 L805,290" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M755,310 L805,310" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- Layer 1' 方框 -->
    <rect x="805" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- Layer 1' 神经元 - 灰色圆点 -->
    <circle cx="830" cy="170" r="6" fill="#808080"/>
    <circle cx="830" cy="190" r="6" fill="#808080"/>
    <circle cx="830" cy="210" r="6" fill="#808080"/>
    <circle cx="830" cy="230" r="6" fill="#808080"/>
    <circle cx="830" cy="250" r="6" fill="#808080"/>
    <circle cx="830" cy="270" r="6" fill="#808080"/>
    <circle cx="830" cy="290" r="6" fill="#808080"/>
    <circle cx="830" cy="310" r="6" fill="#808080"/>
    
    <text x="830" y="345" text-anchor="middle" font-family="Arial" font-size="12">v¹</text>
    <text x="830" y="390" text-anchor="middle" font-family="Arial" font-size="12">K1</text>
  </g>

  <!-- 权重连接和输出层 -->
  <g id="output-layer">
    <text x="870" y="130" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">W⁰ᵥ</text>
    <!-- 连接线从Layer 1'到输出层 -->
    <path d="M855,170 L905,170" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M855,170 L905,190" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M855,310 L905,290" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    <path d="M855,310 L905,310" stroke="black" stroke-width="0.5" stroke-opacity="0.3"/>
    
    <!-- 输出层方框 -->
    <rect x="905" y="150" width="50" height="180" rx="5" ry="5" stroke="black" stroke-width="1.5" fill="white"/>
    <!-- 输出层神经元 - 黑色圆点 -->
    <circle cx="930" cy="170" r="6" fill="black"/>
    <circle cx="930" cy="190" r="6" fill="black"/>
    <circle cx="930" cy="210" r="6" fill="black"/>
    <circle cx="930" cy="230" r="6" fill="black"/>
    <circle cx="930" cy="250" r="6" fill="black"/>
    <circle cx="930" cy="270" r="6" fill="black"/>
    <circle cx="930" cy="290" r="6" fill="black"/>
    <circle cx="930" cy="310" r="6" fill="black"/>
    
    <text x="930" y="345" text-anchor="middle" font-family="Arial" font-size="12">v⁰</text>
    <text x="930" y="365" text-anchor="middle" font-family="Arial" font-size="12">90</text>
    
    <!-- Reconstruction Data标签和箭头 -->
    <text x="930" y="400" text-anchor="middle" font-family="Arial" font-size="12">Reconstruction</text>
    <text x="930" y="415" text-anchor="middle" font-family="Arial" font-size="12">Data</text>
    <path d="M930,385 L930,370" stroke="#3D9970" stroke-width="2" fill="none" marker-end="url(#arrowhead)"/>
  </g>

  <!-- 底部连接弧线和损失函数 ε_j -->
  <g id="loss-function">
    <path d="M120,550 L930,550" stroke="black" stroke-width="2" fill="none"/>
    <path d="M120,350 L120,550" stroke="black" stroke-width="2" fill="none"/>
    <path d="M930,350 L930,550" stroke="black" stroke-width="2" fill="none"/>
    
    <!-- 损失函数框 -->
    <rect x="500" y="520" width="50" height="30" rx="10" ry="10" stroke="black" stroke-width="1.5" fill="white"/>
    <text x="525" y="540" text-anchor="middle" font-family="Arial" font-size="14" font-style="italic">ε_j</text>
  </g>

  <!-- 箭头定义 -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#3D9970"/>
    </marker>
  </defs>
</svg>