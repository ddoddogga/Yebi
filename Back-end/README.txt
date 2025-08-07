―――――――――― 서버 실행 방법 ――――――――――
ㆍngrok 실행

ㆍngrok 인증 토큰 등록하기
ngrok config add-authtoken [토큰]

ㆍFastAPI 서버 실행하기
uvicorn Server:app --reload

ㆍngrok의 새 탭에서 FastAPI 서버 외부 공개하기 (파일 경로는 예시임)
& "C:\Users\yjh71\Desktop\JH\공모전\Back-end\ngrok.exe" http 8000

ㆍ카카오 오픈빌더에 Forwarding 주소 등록하기 (주소는 예시임)
https://e8fd36ae5209.ngrok-free.app/webhook