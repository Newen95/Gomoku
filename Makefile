SRC		=	src/

NAME 	=	pbrain-gomoku-ai

PRINT	=	@echo -e
RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m # No Color

$(NAME):
	@cp $(SRC)main.py $@
	@chmod +x $@
	$(PRINT) "-> ${GREEN}BINARY CREATED${NC}"

all: $(NAME)

clean:
	$(PRINT) "-> ${RED}REMOVE PYCACHE${NC}"
	$(RM) -r __pycache__ $(SRC)__pycache__ $(SRC)command/__pycache__ $(SRC)algorithm/__pycache__

fclean: clean
	$(PRINT) "-> ${RED}REMOVE BINARY${NC}"
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean tests_run re