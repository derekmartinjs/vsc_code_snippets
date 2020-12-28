tag: browser
-
(address bar | go url | go address): browser.focus_address()
go home: browser.go_home()
forward: browser.go_forward()

duplicate it:
  key(cmd-l)
  key(cmd-enter)
  user.tab_final()

go back[ward]: browser.go_back()

go private: browser.open_private_window()

bookmark show: browser.bookmarks()
bookmark bar: browser.bookmarks_bar()
bookmark it: browser.bookmark()
bookmark tabs: browser.bookmark_tabs()

#show terminal: browser.terminal()

^algorithms course$:
  key(cmd-t)
  insert("https://www.educative.io/courses/grokking-the-coding-interview")
  key(enter)

^leetcode [problems]$:
  key(cmd-t)
  insert("https://leetcode.com/problemset/all/")
  key(enter)


^the atlantic:
  key(cmd-t)
  insert("theatlantic.com")
  key(enter)

news:
  key(cmd-t)
  insert("f5oclock.com")
  key(enter)

^amazon [orders]$:
  key(cmd-t)
  insert("https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first")
  key(enter)

(refresh | reload) it: browser.reload()
(refresh | reload) it hard: browser.reload_hard()

# b-ok search 
#show downloads: browser.show_downloads()
#show extensions: browser.show_extension()
#show history: browser.show_history()
#show cache: browser.show_clear_cache()

#dev_tools: browser.toggle_dev_tools()
#show device mode: browser.show_clear_cache()
#inspect element: browser.inspect_element()
