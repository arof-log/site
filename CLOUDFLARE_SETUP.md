# Cloudflare Pages 배포 설정

이 저장소는 HTML/CSS/JavaScript + Pages CMS의 작품별 JSON 파일을 사용합니다.
새 프레임워크나 외부 DB가 필요하지 않습니다.

## Cloudflare Pages 연결
1. https://dash.cloudflare.com/ 에 로그인합니다.
2. Workers & Pages에서 Pages 프로젝트를 생성하고 **Connect to Git**을 선택합니다.
3. GitHub 저장소 `arof-log/site`을 연결합니다.
4. Production branch를 `main`으로 선택합니다.
5. 빌드 설정을 다음과 같이 입력합니다.

| Cloudflare 설정 | 입력 값 |
|---|---|
| Framework preset | None |
| Root directory | / (저장소 루트) |
| Build command | `bash scripts/build_cloudflare.sh` |
| Build output directory | `_site` |
| Environment variables | 필요 없음 |

6. **Save and Deploy**를 선택합니다.
7. Cloudflare에서 발급하는 `*.pages.dev` 주소로 사이트를 확인합니다.

## CMS 데이터 배포 구조
Pages CMS의 Works 수정 → GitHub `main` 브랜치에 JSON 커밋 →
Cloudflare Pages Git integration 빌드 →
`scripts/build_cloudflare.sh` →
`scripts/build_works.py` → `_site/works.json` 생성 →
`js/script.js`에서 읽어 기존 Works 카드에 반영

- 작품은 `content/works/work-*.json`에 각각 저장됩니다.
- `.pages.yml`의 Works Collection이 해당 폴더를 관리합니다.
- `published`와 `featured`가 모두 true인 작품이 메인 Works 목록에 노출됩니다.
- 번호와 순서는 `order`로 제어됩니다.
- 사이트의 HTML/CSS와 기존 Swiper/Fancybox 인터랙션을 유지합니다.
- 외부 이미지 URL은 유지되며, CMS에서 `images/`에 업로드한 파일은 상대 경로로 표시됩니다.
- 기존 상세페이지 링크 대상 `detail-*.html` 파일은 아직 확인되지 않았으므로 별도 추가가 필요합니다.

## 주의 및 검증
- GitHub Pages용 기존 workflow는 삭제하지 않았습니다. Cloudflare Pages와 별도로 작동할 수 있습니다.
- Cloudflare Pages는 GitHub 저장소 연결과 배포 권한 승인이 필요합니다. 저장소에 파일을 올리는 것만으로 배포가 시작되지 않습니다.
- Cloudflare에서 **배포 성공**을 확인하고 `/works.json` 주소에서 JSON 데이터가 나오는지 확인하세요.
- 브라우저 Works 카드가 CMS 데이터와 일치하는지 확인하세요.
- Pages CMS 편집기는 https://app.pagescms.org/ 에서 연결 후 확인합니다.
