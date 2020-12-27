# 패키지를 읽어 들일 때 가장 먼저 실행
# from <패키지 이름> import * 할 때 __all__에 저장한 모듈들이 전부 읽어 들여짐
__all__ = ["module_a", "module_b"]

print("test_package를 읽어들였습니다")