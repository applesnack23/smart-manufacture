# APPENDIX — 라즈베리파이 배포 이미지

교재 실습용 라즈베리파이 제로 v1.3 의 OS 이미지입니다. Raspberry Pi OS · USB 가젯(192.168.7.1) · Python 3.13.5 · gpiozero · OpenPLC 런타임 · 공유 폴더(Samba) · `~/projects/PART05 ~ PART07` 이 모두 설정되어 있습니다.

## 받기
- 링크: https://vo.la/ZUvFmAM (구글 드라이브)
- 「다운로드」 → 「무시하고 다운로드」 를 누릅니다. zip 이면 압축을 풀지 않아도 됩니다.
- 파일이 커서(약 4 GB) GitHub 에는 올리지 않고 링크로만 공유합니다.

## SD 카드에 굽기 (Raspberry Pi Imager)
1. Raspberry Pi Imager 실행 (https://www.raspberrypi.com/software/)
2. 장치: **Raspberry Pi Zero**
3. 운영체제: 맨 아래 **Use custom (사용자 정의)** → 받은 이미지 파일 선택
4. 저장소: SD 카드 선택 — **8 GB 이상**, 용량으로 꼭 확인 (다른 USB 를 고르면 지워짐)
5. 「OS 커스터마이징 설정을 적용할까요?」 → **아니요**
6. 쓰기 · 검증이 끝나면 SD 카드를 라즈베리파이에 꽂습니다. 첫 부팅은 SD 크기에 맞춰 영역을 늘리느라 조금 더 걸립니다.

## 접속
- 라즈베리파이의 「USB」 포트(PWR IN 아님)를 데이터용 케이블로 PC 에 연결하고 1~2 분 기다립니다.
- PC 명령 프롬프트: `ssh twiniex@192.168.7.1`
- **로그인 이름은 `twiniex`** 입니다. 교재에서 `username` 으로 적은 곳은 모두 `twiniex` 로 바꿔 입력합니다.
- 비밀번호는 선생님이 알려 줍니다.
- 공유 폴더: 탐색기 주소창 `\\192.168.7.1\projects`
- OpenPLC 웹: http://192.168.7.1:8080 (openplc / openplc)

자세한 내용은 교재 PART 04 5-2 와 부록 4 장을 봅니다.
