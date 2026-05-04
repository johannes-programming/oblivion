.PHONY: zip clean

ZIP := dist/oblivion.zip
SRC_DIR := src/oblivion

zip: $(ZIP)

$(ZIP): $(SRC_DIR)
	@mkdir -p $(dir $(ZIP))
	@rm -f $(ZIP)
	@cd $(SRC_DIR) && zip -rq ../../$(ZIP) . -x ".*" "*/.*"

clean:
	@rm -f $(ZIP)
