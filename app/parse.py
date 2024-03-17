from bs4 import BeautifulSoup

from app.gpt import get_desc
from fetch import get_page


# Your HTML snippet

extracted_data = []

def parse_data():
    global extracted_data
    extracted_data.clear()

    try:
        html_snippet = get_page()
        # Parse the HTML
        soup = BeautifulSoup(html_snippet, 'html.parser')

        # Initialize a list to store extracted data

        # article 示例
        # <article class="Box-row">
        #   <div class="float-right d-flex">
        #
        #       <template class="js-unstar-confirmation-dialog-template">
        #   <div class="Box-header">
        #     <h2 class="Box-title">Unstar this repository?</h2>
        #   </div>
        #   <div class="Box-body">
        #     <p class="mb-3">
        #       This will remove {{ repoNameWithOwner }} from the {{ listsWithCount }} that it's been added to.
        #     </p>
        #     <div class="form-actions">
        #       <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-confirmation-form" data-turbo="false" action="{{ confirmUrl }}" accept-charset="UTF-8" method="post">
        #         <input type="hidden" name="authenticity_token" value="{{ confirmCsrfToken }}">
        #         <input type="hidden" name="confirm" value="true">
        #           <button data-close-dialog="true" type="submit" data-view-component="true" class="btn-danger btn width-full">    Unstar
        # </button>
        # </form>    </div>
        #   </div>
        # </template>
        #
        #   <div data-view-component="true" class="js-toggler-container js-social-container starring-container d-flex">
        #     <div data-view-component="true" class="starred BtnGroup flex-1 ml-0">
        #       <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto js-deferred-toggler-target" data-turbo="false" action="/slint-ui/slint/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="L-WjfYkdmuNhdoOCywpmoObjcUlXdEdEeV_VJpxsk_2DdUSJHzLVBu05CK14XOZALDKPneSLe2fAlH9EIkn25Q" autocomplete="off">
        #           <input type="hidden" value="_n72IuKRZdKsOWkNqCG2LAOaOkYfCIw6Mpg55pCYalZS7hHWdL4qNyB24iIbdzbMyUvEkqz3sBmLU5OELr0PTg" data-csrf="true" class="js-confirm-csrf-token">
        #         <input type="hidden" name="context" value="trending">
        #           <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:261124045,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:49626730}}" data-hydro-click-hmac="1ef49d56f2d50cb242cf3e352ec55319e681272e893542c2f633c837d03c66b8" data-ga-click="Repository, click unstar button, action:trending#index; text:Unstar" aria-label="Unstar this repository" type="submit" data-view-component="true" class="rounded-left-2 btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill starred-button-icon d-none d-md-inline-block mr-2">
        #     <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"></path>
        # </svg><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star-fill starred-button-icon mr-0 d-inline-block d-md-none">
        #     <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"></path>
        # </svg>
        #             <span data-view-component="true" class="d-none d-md-inline">
        #               Starred
        # </span>
        # </button></form>        <details id="details-user-list-261124045-starred" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-inline-block position-relative">
        #         <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
        #     <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
        # </svg>
        # </summary>
        #   <details-menu class="SelectMenu right-0" src="/slint-ui/slint/lists" role="menu">
        #     <div class="SelectMenu-modal">
        #         <header class="SelectMenu-header">
        #                 <h4 class="SelectMenu-title f5" id="user-lists-menu">Lists</h4>
        #
        #           <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-toggle-for="details-user-list-261124045-starred">
        #             <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
        #     <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
        # </svg>
        #           </button>
        #         </header>
        #       <div id="filter-menu-7608f0" class="d-flex flex-column flex-1 overflow-hidden">
        #         <div class="SelectMenu-list">
        #
        #             <include-fragment class="SelectMenu-loading" aria-label="Loading">
        #               <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
        #   <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
        #   <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
        # </svg>
        #             </include-fragment>
        #         </div>
        #
        #       </div>
        #     </div>
        #   </details-menu>
        # </details>
        # </div>
        #     <div data-view-component="true" class="unstarred BtnGroup ml-0 flex-1">
        #       <!-- '"` --><!-- </textarea></xmp> --><form class="js-social-form BtnGroup-parent flex-auto" data-turbo="false" action="/slint-ui/slint/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="yOC-pLzfnys2ieYxHBamdf82cWsgA8Nzl5_eGC4OkaZURtCel_Lf0ftmtnekQBBGyRyMXBhNjH0AXKJ05L-WXg" autocomplete="off">
        #         <input type="hidden" name="context" value="trending">
        #           <button data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:261124045,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:49626730}}" data-hydro-click-hmac="bc781bb0aa5e3c615609455903c4276deb41773bd242f5c6aa69d3b5ffa173ee" data-ga-click="Repository, click star button, action:trending#index; text:Star" aria-label="Star this repository" type="submit" data-view-component="true" class="js-toggler-target rounded-left-2 btn-sm btn BtnGroup-item">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star d-none d-md-inline-block mr-2">
        #     <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
        # </svg><svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star mr-0 d-inline-block d-md-none">
        #     <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
        # </svg>
        #             <span data-view-component="true" class="d-none d-md-inline">
        #               Star
        # </span>
        # </button></form>        <details id="details-user-list-261124045-unstarred" data-view-component="true" class="details-reset details-overlay BtnGroup-parent js-user-list-menu d-inline-block position-relative">
        #         <summary aria-label="Add this repository to a list" data-view-component="true" class="btn-sm btn BtnGroup-item px-2 float-none" aria-haspopup="menu" role="button">    <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-triangle-down">
        #     <path d="m4.427 7.427 3.396 3.396a.25.25 0 0 0 .354 0l3.396-3.396A.25.25 0 0 0 11.396 7H4.604a.25.25 0 0 0-.177.427Z"></path>
        # </svg>
        # </summary>
        #   <details-menu class="SelectMenu right-0" src="/slint-ui/slint/lists" role="menu">
        #     <div class="SelectMenu-modal">
        #         <header class="SelectMenu-header">
        #                 <h4 class="SelectMenu-title f5" id="user-lists-menu">Lists</h4>
        #
        #           <button class="SelectMenu-closeButton" type="button" aria-label="Close menu" data-toggle-for="details-user-list-261124045-unstarred">
        #             <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-x">
        #     <path d="M3.72 3.72a.75.75 0 0 1 1.06 0L8 6.94l3.22-3.22a.749.749 0 0 1 1.275.326.749.749 0 0 1-.215.734L9.06 8l3.22 3.22a.749.749 0 0 1-.326 1.275.749.749 0 0 1-.734-.215L8 9.06l-3.22 3.22a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L6.94 8 3.72 4.78a.75.75 0 0 1 0-1.06Z"></path>
        # </svg>
        #           </button>
        #         </header>
        #       <div id="filter-menu-19015f" class="d-flex flex-column flex-1 overflow-hidden">
        #         <div class="SelectMenu-list">
        #
        #             <include-fragment class="SelectMenu-loading" aria-label="Loading">
        #               <svg role="menuitem" style="box-sizing: content-box; color: var(--color-icon-primary);" width="32" height="32" viewBox="0 0 16 16" fill="none" data-view-component="true" class="anim-rotate">
        #   <circle cx="8" cy="8" r="7" stroke="currentColor" stroke-opacity="0.25" stroke-width="2" vector-effect="non-scaling-stroke" fill="none"></circle>
        #   <path d="M15 8a7.002 7.002 0 00-7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
        # </svg>
        #             </include-fragment>
        #         </div>
        #
        #       </div>
        #     </div>
        #   </details-menu>
        # </details>
        # </div></div>
        #   </div>
        #
        #   <h2 class="h3 lh-condensed">
        #     <a data-hydro-click="{&quot;event_type&quot;:&quot;explore.click&quot;,&quot;payload&quot;:{&quot;click_context&quot;:&quot;TRENDING_REPOSITORIES_PAGE&quot;,&quot;click_target&quot;:&quot;REPOSITORY&quot;,&quot;click_visual_representation&quot;:&quot;REPOSITORY_NAME_HEADING&quot;,&quot;actor_id&quot;:49626730,&quot;record_id&quot;:261124045,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:49626730}}" data-hydro-click-hmac="055301820bcff0bf11fdfb3978a7c4263d13d1ebee499ccd92f7fd20d5bc8da4" href="/slint-ui/slint" data-view-component="true" class="Link">
        #       <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo mr-1 color-fg-muted">
        #     <path d="M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z"></path>
        # </svg>
        #
        #       <span data-view-component="true" class="text-normal">
        #         slint-ui /
        # </span>
        #       slint
        # </a>  </h2>
        #
        #     <p class="col-9 color-fg-muted my-1 pr-4">
        #       Slint is a declarative GUI toolkit to build native user interfaces for Rust, C++, or JavaScript apps.
        #     </p>
        #
        #   <div class="f6 color-fg-muted mt-2">
        #       <span class="d-inline-block ml-0 mr-3">
        #   <span class="repo-language-color" style="background-color: #dea584"></span>
        #   <span itemprop="programmingLanguage">Rust</span>
        # </span>
        #
        #
        #       <a href="/slint-ui/slint/stargazers" data-view-component="true" class="Link Link--muted d-inline-block mr-3">
        #         <svg aria-label="star" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
        #     <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
        # </svg>
        #         14,258
        # </a>
        #       <a href="/slint-ui/slint/forks" data-view-component="true" class="Link Link--muted d-inline-block mr-3">
        #         <svg aria-label="fork" role="img" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-repo-forked">
        #     <path d="M5 5.372v.878c0 .414.336.75.75.75h4.5a.75.75 0 0 0 .75-.75v-.878a2.25 2.25 0 1 1 1.5 0v.878a2.25 2.25 0 0 1-2.25 2.25h-1.5v2.128a2.251 2.251 0 1 1-1.5 0V8.5h-1.5A2.25 2.25 0 0 1 3.5 6.25v-.878a2.25 2.25 0 1 1 1.5 0ZM5 3.25a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Zm6.75.75a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Zm-3 8.75a.75.75 0 1 0-1.5 0 .75.75 0 0 0 1.5 0Z"></path>
        # </svg>
        #         436
        # </a>
        #       <span data-view-component="true" class="d-inline-block mr-3">
        #         Built by
        #
        #           <a class="d-inline-block" data-hydro-click="{&quot;event_type&quot;:&quot;explore.click&quot;,&quot;payload&quot;:{&quot;click_context&quot;:&quot;TRENDING_REPOSITORIES_PAGE&quot;,&quot;click_target&quot;:&quot;CONTRIBUTING_DEVELOPER&quot;,&quot;click_visual_representation&quot;:&quot;DEVELOPER_AVATAR&quot;,&quot;actor_id&quot;:null,&quot;record_id&quot;:null,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:152718985}}" data-hydro-click-hmac="8a5727b3759932942798f9b0ec3d6f930879a678eefdb44d01957672d05d1f21" data-hovercard-type="user" data-hovercard-url="/users/tronical/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/tronical"><img class="avatar mb-1 avatar-user" src="https://avatars.githubusercontent.com/u/1486?s=40&amp;v=4" width="20" height="20" alt="@tronical"></a>
        #           <a class="d-inline-block" data-hydro-click="{&quot;event_type&quot;:&quot;explore.click&quot;,&quot;payload&quot;:{&quot;click_context&quot;:&quot;TRENDING_REPOSITORIES_PAGE&quot;,&quot;click_target&quot;:&quot;CONTRIBUTING_DEVELOPER&quot;,&quot;click_visual_representation&quot;:&quot;DEVELOPER_AVATAR&quot;,&quot;actor_id&quot;:null,&quot;record_id&quot;:null,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:152718985}}" data-hydro-click-hmac="8a5727b3759932942798f9b0ec3d6f930879a678eefdb44d01957672d05d1f21" data-hovercard-type="user" data-hovercard-url="/users/ogoffart/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/ogoffart"><img class="avatar mb-1 avatar-user" src="https://avatars.githubusercontent.com/u/959326?s=40&amp;v=4" width="20" height="20" alt="@ogoffart"></a>
        #           <a class="d-inline-block" data-hydro-click="{&quot;event_type&quot;:&quot;explore.click&quot;,&quot;payload&quot;:{&quot;click_context&quot;:&quot;TRENDING_REPOSITORIES_PAGE&quot;,&quot;click_target&quot;:&quot;CONTRIBUTING_DEVELOPER&quot;,&quot;click_visual_representation&quot;:&quot;DEVELOPER_AVATAR&quot;,&quot;actor_id&quot;:null,&quot;record_id&quot;:null,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:152718985}}" data-hydro-click-hmac="8a5727b3759932942798f9b0ec3d6f930879a678eefdb44d01957672d05d1f21" data-hovercard-type="user" data-hovercard-url="/users/hunger/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/hunger"><img class="avatar mb-1 avatar-user" src="https://avatars.githubusercontent.com/u/73267?s=40&amp;v=4" width="20" height="20" alt="@hunger"></a>
        #           <a class="d-inline-block" data-hydro-click="{&quot;event_type&quot;:&quot;explore.click&quot;,&quot;payload&quot;:{&quot;click_context&quot;:&quot;TRENDING_REPOSITORIES_PAGE&quot;,&quot;click_target&quot;:&quot;CONTRIBUTING_DEVELOPER&quot;,&quot;click_visual_representation&quot;:&quot;DEVELOPER_AVATAR&quot;,&quot;actor_id&quot;:null,&quot;record_id&quot;:null,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:152718985}}" data-hydro-click-hmac="8a5727b3759932942798f9b0ec3d6f930879a678eefdb44d01957672d05d1f21" data-hovercard-type="user" data-hovercard-url="/users/FloVanGH/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/FloVanGH"><img class="avatar mb-1 avatar-user" src="https://avatars.githubusercontent.com/u/6715107?s=40&amp;v=4" width="20" height="20" alt="@FloVanGH"></a>
        #           <a class="d-inline-block" data-hydro-click="{&quot;event_type&quot;:&quot;explore.click&quot;,&quot;payload&quot;:{&quot;click_context&quot;:&quot;TRENDING_REPOSITORIES_PAGE&quot;,&quot;click_target&quot;:&quot;CONTRIBUTING_DEVELOPER&quot;,&quot;click_visual_representation&quot;:&quot;DEVELOPER_AVATAR&quot;,&quot;actor_id&quot;:null,&quot;record_id&quot;:null,&quot;originating_url&quot;:&quot;https://github.com/trending&quot;,&quot;user_id&quot;:152718985}}" data-hydro-click-hmac="8a5727b3759932942798f9b0ec3d6f930879a678eefdb44d01957672d05d1f21" data-hovercard-type="user" data-hovercard-url="/users/lukas-jung/hovercard" data-octo-click="hovercard-link-click" data-octo-dimensions="link_type:self" href="/lukas-jung"><img class="avatar mb-1 avatar-user" src="https://avatars.githubusercontent.com/u/22800467?s=40&amp;v=4" width="20" height="20" alt="@lukas-jung"></a>
        # </span>
        #       <span data-view-component="true" class="d-inline-block float-sm-right">
        #         <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-star">
        #     <path d="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z"></path>
        # </svg>
        #         42 stars today
        # </span>  </div>
        # </article>
        # Iterate over each article tag
        for article in soup.find_all('article', class_='Box-row'):
        # Extract the repository name
            repo_name = article.find('h2').text.strip()
            # 去除 repo_name 中的所有空白
            repo_name = "".join(repo_name.split())

            # Extract the URL
            url_suffix = article.find('h2').find('a')['href']
            url = f"https://github.com{url_suffix}"

            description = get_desc(repo_name)
            print(description)
            if description == "":
                # Extract the repository description
                description = article.find('p', class_='color-fg-muted').text.strip() if article.find('p', class_='color-fg-muted') else "No description"

            # 获取 article 中的 programmingLanguage
            programmingLanguage = article.find('span', itemprop='programmingLanguage').text.strip() if article.find('span', itemprop='programmingLanguage') else "No programmingLanguage"

            # 获取 article 中的 octicon-star
            star = article.find('a', href=f"{url_suffix}/stargazers").text.strip() if article.find('a', href=f"{url_suffix}/stargazers") else "No star"

            # 获取 repo-language-color 类 的 background-color 属性
            repo_language_color = article.find('span', class_='repo-language-color')['style'].split(':')[1].strip() if article.find('span', class_='repo-language-color') else "No color"

            # Append the extracted information to the list
            extracted_data.append({'name': repo_name, 'description': description, 'url': url,
                                   'programmingLanguage': programmingLanguage,
                                   'stars': star,
                                   'repo_language_color': repo_language_color})
        # print(extracted_data)
    except Exception as e:
        extracted_data.clear()
        print(e)

