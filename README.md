
## 📌 프로젝트 개요
터미널에서 메뉴 번호를 입력해 AI 프롬프트를 관리하는 콘솔 기반 Python 프로그램입니다.

---

## ✅ 전체 과업 체크리스트

---

## 1단계: 개발 환경 설정

- [ ] VSCode 설치
- [ ] Python 확장(Extension) 설치
- [ ] Korean Language Pack 설치 (선택)
- [ ] Python 3.10 이상 설치 확인
  ```bash
  PS C:\A1-1> python --version
     Python 3.14.6
  ```
- [ ] print("Hello") 실행 테스트
  ```bash
    PS C:\A1-1> & C:\Users\DiCiA\AppData\Local\Python\pythoncore-3.14-64\python.exe c:/A1-1/main.py
    hello world
    This is a sample Python script.
  ```
- [ ] Git 설치 확인
  ```bash
  PS C:\A1-1> git --version
  git version 2.54.0.windows.1
  ```
- [ ] Git 사용자 정보 설정
  ```bash
  PS C:\A1-1> git config --global user.name "장상민"
  PS C:\A1-1> git config --global user.email "smz7093@hanmail.net"
  ```
- [ ] 기본 브랜치 main 설정
  ```bash
  git config --global init.defaultBranch main
  ```
- [ ] VSCode에서 GitHub 계정 로그인 연동

---

## 2단계: GitHub 저장소 설정

- [ ] GitHub에서 새 저장소(Repository) 생성
- [ ] 로컬 프로젝트 폴더 생성
- [ ] git init 실행
  ```bash
  git init
  ```
- [ ] 원격 저장소 연결
  ```bash
  git remote add origin [https://github.com/smz7093-web/A1-1]
  ```
- [ ] .gitignore 파일 생성
- [ ] README.md 파일 생성 (프로젝트 제목 작성)
- [ ] 첫 커밋 및 푸시
  ```bash
  git add .
  git commit -m "초기 설정"
  git push origin main
  ```
<img width="930" height="324" alt="image" src="https://github.com/user-attachments/assets/8ff55aff-a03c-4c52-8f15-e7d273024ff5" />
  
- [ ] 공개 샘플 저장소 clone 해보기 (확인 후 삭제 가능)
  ```bash
  git clone [https://github.com/smz7093-web/A1-1]
  ```

---

## 3단계: Python 프로그램 작성

### 구현할 함수 목록

| 함수명 | 역할 |
|--------|------|
| `show_menu()` | 메뉴 출력 |
| `add_prompt()` | 프롬프트 추가 |
| `show_list()` | 전체 목록 보기 |
| `show_by_category()` | 카테고리별 조회 |
| `search_prompt()` | 키워드 검색 |
| `show_detail()` | 상세 보기 |
| `toggle_favorite()` | 즐겨찾기 추가/해제 |
| `show_favorites()` | 즐겨찾기 목록 보기 |
| `main()` | 메인 실행 루프 |

### 기본 데이터 구조

```python
# 각 프롬프트는 아래 형태의 딕셔너리로 저장
{
    "title": "제목",
    "content": "내용",
    "category": "카테고리",
    "favorite": False
}
```

### 기본 데이터 요건

- [ ] 이전 미션에서 작성한 프롬프트 최소 3개 등록
- [ ] 카테고리 목록 정의
  - 텍스트 생성
  - 이미지 생성
  - 영상 생성
  - 페르소나
  - 자동화
  - 기타

### 각 기능 요건

- [ ] 메뉴: 번호 입력으로 선택, 잘못된 입력 시 재출력
- [ ] 추가: 빈 입력 시 재요청, 즐겨찾기 기본값 False
- [ ] 목록: 번호, 제목, 카테고리, ⭐ 표시
- [ ] 카테고리 조회: 카테고리 선택 후 해당 목록 출력
- [ ] 검색: 제목 + 내용 포함 검색, 결과 없으면 안내 메시지
- [ ] 상세 보기: 번호 입력, 잘못된 번호 입력 시 안내 메시지
- [ ] 즐겨찾기: 번호 입력으로 토글 (추가/해제)

---

## 4단계: 브랜치 작업 (필수)

- [ ] 새 브랜치 생성 및 이동
  ```bash
  git checkout -b feature/show-list
  ```
- [ ] `show_list()` 기능 해당 브랜치에서 작업
- [ ] 작업 완료 후 커밋
  ```bash
  git add .
  git commit -m "feat: show_list() 전체 목록 보기 구현"
  ```
- [ ] main 브랜치로 전환
  ```bash
  git checkout main
  ```
- [ ] 브랜치 병합
  ```bash
  git merge feature/show-list
  ```
- [ ] GitHub에 푸시
  ```bash
  git push origin main
  ```

---

## 5단계: 커밋 관리 (최소 10개)

| 순서 | 커밋 메시지 예시 |
|------|----------------|
| 1 | `init: 프로젝트 초기 설정, .gitignore, README 추가` |
| 2 | `feat: 기본 데이터 및 카테고리 목록 추가` |
| 3 | `feat: show_menu() 메인 루프 구현` |
| 4 | `feat: add_prompt() 프롬프트 추가 기능 구현` |
| 5 | `feat: show_list() 전체 목록 보기 구현 (feature 브랜치)` |
| 6 | `merge: feature/show-list → main 병합` |
| 7 | `feat: show_by_category() 카테고리 조회 구현` |
| 8 | `feat: search_prompt() 검색 기능 구현` |
| 9 | `feat: show_detail() 상세 보기 구현` |
| 10 | `feat: toggle_favorite(), show_favorites() 즐겨찾기 구현` |
| 11 | `docs: README.md 최종 업데이트` |

---

## 6단계: README.md 작성 항목

- [ ] 프로그램 이름 및 설명
- [ ] 실행 방법
  ```bash
  python main.py
  ```
- [ ] 기능 목록
- [ ] 카테고리 설명
- [ ] 프롬프트 예시 (선택)

---

## 7단계: 제출 준비

- [ ] GitHub 저장소 URL 확인
- [ ] 스크린샷 준비
  - VSCode 화면 (Python 버전, Git 설정 확인)
  - 프로그램 실행 결과 (메뉴, 추가, 목록, 검색 화면)
  - git log 결과
    ```bash
    git log --oneline --graph
    ```

---

## ⚠️ 필수 Git 명령어 사용 체크

| 명령어 | 사용 시점 | 완료 |
|--------|----------|------|
| `git init` | 로컬 저장소 초기화 | [ ] |
| `git add` | 변경 파일 스테이징 | [ ] |
| `git commit` | 커밋 생성 | [ ] |
| `git push` | GitHub 업로드 | [ ] |
| `git pull` | 원격 변경사항 받기 | [ ] |
| `git checkout` | 브랜치 전환/생성 | [ ] |
| `git clone` | 샘플 저장소 복제 | [ ] |
| `git merge` | 브랜치 병합 | [ ] |

---

## 🚀 실행 방법

```bash
python main.py
```

## 📂 프로젝트 구조

```
project/
├── main.py         # 메인 프로그램
├── .gitignore      # Git 제외 파일 목록
└── README.md       # 프로젝트 설명서
```
```

