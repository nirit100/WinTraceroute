dist:
	mkdir dist

_dist_out:
	mkdir -f _dist_out
	mkdir -f _dist_out/win
	mkdir -f _dist_out/lnx


clean:	dist _dist_out/
	rm -f dist/*
	rm -rf logs/


build_lnx:	clean
	pyinstaller -c --clean --onefile traceroute/__main__.py
	cp -f -T "dist/__main__" "_dist_out/lnx/wintraceroute"

# not in use currently
build_win:	clean
	pyinstaller -c --clean --uac-admin --onefile traceroute/__main__.py
	cp -f -T "dist/__main__.exe" "_dist_out/win/wintraceroute.exe"
