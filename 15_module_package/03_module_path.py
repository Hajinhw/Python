import sys

for path in sys.path:
    print(path)


# 파이썬 모듈 검색 경로
# 1. sys.module
# 2. built_in_modules
# 3. sys.path

# sys.path.append('새로운 모듈 파일 경로')