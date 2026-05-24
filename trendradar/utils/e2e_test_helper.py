# coding=utf-8
# E2E 测试辅助模块

def validate_input(data):
    """验证输入数据"""
    if data is None:
        return False
    if not isinstance(data, dict):
        return False
    return True

def process_items(items, threshold=0.5):
    """处理数据项列表"""
    if items is None:
        return []
    result = []
    for item in items:
        if item.get("score", 0) >= threshold:
            result.append(item)
    return result

class DataProcessor:
    def __init__(self, config=None):
        self.config = config or {}
        self.data = []
    
    def load(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            self.data = content.split("\n")
        except FileNotFoundError:
            self.data = []
    
    def process(self):
        if not self.data:
            return []
        return [line.strip() for line in self.data if line.strip()]
