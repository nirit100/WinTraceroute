dist:
	mkdir dist

_dist_out:
	mkdir -p _dist_out/win
	mkdir -p _dist_out/lnx


clean:	dist _dist_out
	sudo rm -rf dist/*
	rm -rf logs/


build_lnx:	clean
	pyinstaller -c --clean --onefile traceroute/__main__.py
	cp -t "_dist_out/lnx/" "dist/"*
	mv "_dist_out/lnx/__main__" "_dist_out/lnx/wintraceroute"

# not in use currently
build_win:	clean
	pyinstaller -c --clean --uac-admin --onefile traceroute/__main__.py
	cp -t "./_dist_out/win/" "./dist/"*
	mv "_dist_out/win/__main__.exe" "_dist_out/win/wintraceroute.exe"

build_py:	clean
	python3 -m build

upload_pypi:	build_py
	twine upload dist/* -u "$(PYPI_UNAME)" -p "$(PYPI_PASSWD)" --non-interactive --disable-progress-bar --skip-existing --verbose

spec-remove-hooksconfig:
	sed -i '/hooksconfig/d' __main__.spec
