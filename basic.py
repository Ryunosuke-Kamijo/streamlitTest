import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 入門')

st.write('Data Frame')

# 1. 表
df = pd.DataFrame({
    '1列目': [0.1, 0.2, 0.3, 0.4],
    '2列目': [1, 2, 3, 4],
})
# st.dataframeや、st.writeでも書ける
st.table(df.style.highlight_max(axis=0))

# 2. 折れ線グラフ
df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c'],
)
# area_chart、bar_chartなど(Referenseの[Display charts]を参照)
st.line_chart(df)

# 3. マップ
df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.7],
    columns=['lat', 'lon'], # 緯度, 経度
)
# (Referenseの[Display charts]を参照)
st.map(df)

# 4. 画像表示([Display media]を参照)
img = Image.open("C:\\Users\\ryuns\\Downloads\\extras\\1.png")
st.image(img, caption='sample image', use_column_width=True)

# markdownを書くと、webページに反映される
"""
# 章
## 説
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
