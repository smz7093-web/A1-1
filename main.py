# 카테고리 정의
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 프롬프트 데이터 (보너스 과제 2: views 키 추가)
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
        "category": "텍스트 생성",
        "favorite": True,
        "views": 0,
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성하기 위한 미드저니 프롬프트를 작성해주세요: [제품명]",
        "category": "이미지 생성",
        "favorite": False,
        "views": 0,
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 15년 차 시니어 IT 컨설턴트입니다. 비즈니스 문제를 기술적으로 해결하는 관점에서 전문적이고 명확한 조언을 제공해주세요.",
        "category": "페르소나",
        "favorite": False,
        "views": 0,
    },
]


def print_header(title: str) -> None:
    """메뉴 및 기능 헤더를 출력합니다."""
    print(f"\n=== {title} ===")


def select_category(default: str = None) -> str:
    """사용자로부터 카테고리를 선택받습니다."""
    print("\n카테고리 선택:")
    for idx, category in enumerate(CATEGORIES, start=1):
        print(f"{idx}) {category}")

    while True:
        prompt_msg = "선택 (번호 또는 직접 입력)"
        if default:
            prompt_msg += f" [기존: {default}]"
        choice = input(f"{prompt_msg}: ").strip()

        if not choice:
            if default:
                return default
            print("카테고리를 입력해주세요.")
            continue

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(CATEGORIES):
                return CATEGORIES[idx]

        return choice


def add_prompt() -> None:
    """1. 새 프롬프트를 추가합니다."""
    print_header("프롬프트 추가")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0,
    }

    prompts.append(new_prompt)
    print("\n프롬프트가 성공적으로 추가되었습니다!")


def show_list() -> None:
    """2. 전체 프롬프트 목록을 출력합니다."""
    print_header("프롬프트 목록")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for idx, item in enumerate(prompts, start=1):
        star = " ⭐" if item["favorite"] else ""
        views = f" (조회수: {item['views']})"
        print(f"{idx}. [{item['category']}] {item['title']}{star}{views}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def view_by_category() -> None:
    """3. 카테고리별로 프롬프트를 조회합니다."""
    print_header("카테고리별 조회")

    category = select_category()
    filtered = [p for p in prompts if p["category"] == category]

    print(f"\n[{category}] 카테고리 프롬프트:")
    if not filtered:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return

    for idx, item in enumerate(filtered, start=1):
        star = " ⭐" if item["favorite"] else ""
        views = f" (조회수: {item['views']})"
        print(f"{idx}. {item['title']}{star}{views}")

    print(f"\n총 {len(filtered)}개의 프롬프트")


def search_prompt() -> None:
    """4. 키워드로 프롬프트를 검색합니다."""
    print_header("프롬프트 검색")

    keyword = input("검색어: ").strip()
    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = [
        p
        for p in prompts
        if keyword.lower() in p["title"].lower()
        or keyword.lower() in p["content"].lower()
    ]

    print("\n검색 결과:")
    if not results:
        print("검색 결과가 없습니다.")
        return

    for idx, item in enumerate(results, start=1):
        star = " ⭐" if item["favorite"] else ""
        views = f" (조회수: {item['views']})"
        print(f"{idx}. [{item['category']}] {item['title']}{star}{views}")

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def view_detail() -> None:
    """5. 프롬프트의 상세 정보를 출력하고 조회수를 증가시킵니다."""
    print_header("프롬프트 상세 보기")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("\n조회할 프롬프트 번호 입력: ").strip()

    if not choice.isdigit():
        print("올바른 숫자를 입력해주세요.")
        return

    idx = int(choice) - 1
    if not (0 <= idx < len(prompts)):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    item = prompts[idx]
    item["views"] += 1  # 조회수 증가

    star = " ⭐" if item["favorite"] else "선택 안 됨"

    print("\n" + "─" * 40)
    print(f"제목: {item['title']}")
    print(f"카테고리: {item['category']}")
    print(f"즐겨찾기: {star}")
    print(f"조회수: {item['views']}회")
    print("─" * 40)
    print("내용:")
    print(item["content"])
    print("─" * 40)


def edit_prompt() -> None:
    """6. 프롬프트 수정 기능"""
    print_header("프롬프트 수정")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("\n수정할 프롬프트 번호 입력: ").strip()

    if not choice.isdigit():
        print("올바른 숫자를 입력해주세요.")
        return

    idx = int(choice) - 1
    if not (0 <= idx < len(prompts)):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    item = prompts[idx]
    print(f"\n[현재 제목] {item['title']}")
    new_title = input("새 제목 (엔터 입력 시 유지): ").strip()

    print(f"\n[현재 내용] {item['content']}")
    new_content = input("새 내용 (엔터 입력 시 유지): ").strip()

    print(f"\n[현재 카테고리] {item['category']}")
    change_cat = input("카테고리를 변경하시겠습니까? (y/N): ").strip().lower()
    new_category = item["category"]
    if change_cat == "y":
        new_category = select_category(default=item["category"])

    if new_title:
        item["title"] = new_title
    if new_content:
        item["content"] = new_content
    item["category"] = new_category

    print("\n프롬프트가 성공적으로 수정되었습니다!")


def delete_prompt() -> None:
    """7. 프롬프트 삭제 기능"""
    print_header("프롬프트 삭제")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("\n삭제할 프롬프트 번호 입력: ").strip()

    if not choice.isdigit():
        print("올바른 숫자를 입력해주세요.")
        return

    idx = int(choice) - 1
    if not (0 <= idx < len(prompts)):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    target = prompts[idx]
    confirm = (
        input(f"정말로 '{target['title']}' 프롬프트를 삭제하시겠습니까? (y/N): ")
        .strip()
        .lower()
    )

    if confirm == "y":
        prompts.pop(idx)
        print("\n프롬프트가 삭제되었습니다.")
        
    else:
        print("\n삭제가 취소되었습니다.")


def toggle_favorite() -> None:
    """8. 즐겨찾기 상태를 추가/해제합니다."""
    print_header("즐겨찾기 관리")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()
    choice = input("\n즐겨찾기를 설정/해제할 프롬프트 번호 입력: ").strip()

    if not choice.isdigit():
        print("올바른 숫자를 입력해주세요.")
        return

    idx = int(choice) - 1
    if not (0 <= idx < len(prompts)):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    prompts[idx]["favorite"] = not prompts[idx]["favorite"]
    status = "추가" if prompts[idx]["favorite"] else "해제"
    print(
        f"\n'{prompts[idx]['title']}' 프롬프트를 즐겨찾기에서 {status}했습니다!"
    )


def show_favorites() -> None:
    """9. 즐겨찾기된 프롬프트만 출력합니다."""
    print_header("즐겨찾기 목록")

    fav_list = [p for p in prompts if p["favorite"]]

    if not fav_list:
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")
        return

    for idx, item in enumerate(fav_list, start=1):
        print(f"{idx}. [{item['category']}] {item['title']} ⭐ (조회수: {item['views']})")

    print(f"\n총 {len(fav_list)}개의 즐겨찾기")


def show_top_prompts() -> None:
    """10. 조회수 기준 정렬 목록을 출력합니다."""
    print_header("인기 프롬프트 TOP 목록 (조회수 순)")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 조회수 기준 내림차순 정렬
    sorted_prompts = sorted(prompts, key=lambda p: p["views"], reverse=True)

    for rank, item in enumerate(sorted_prompts, start=1):
        star = " ⭐" if item["favorite"] else ""
        print(
            f"{rank}위. [{item['category']}] {item['title']}{star} - 조회수: {item['views']}회"
        )


def show_menu() -> str:
    """메뉴를 표시하고 사용자의 선택을 받습니다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 프롬프트 수정")
    print("7. 프롬프트 삭제")
    print("8. 즐겨찾기 관리")
    print("9. 즐겨찾기 목록")
    print("10. 인기 프롬프트 TOP 목록")
    print("0. 종료")
    return input("선택: ").strip()


def main() -> None:
    """프로그램의 메인 루프입니다."""
    while True:
        menu = show_menu()

        if menu == "1":
            add_prompt()
        elif menu == "2":
            show_list()
        elif menu == "3":
            view_by_category()
        elif menu == "4":
            search_prompt()
        elif menu == "5":
            view_detail()
        elif menu == "6":
            edit_prompt()
        elif menu == "7":
            delete_prompt()
        elif menu == "8":
            toggle_favorite()
        elif menu == "9":
            show_favorites()
        elif menu == "10":
            show_top_prompts()
        elif menu == "0":
            print("\n프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("\n잘못된 선택입니다. 메뉴에 표시된 숫자를 입력해주세요.")


if __name__ == "__main__":
    main()