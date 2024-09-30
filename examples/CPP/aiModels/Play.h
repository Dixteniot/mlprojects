// Play.h


#ifndef PLAY_H
#define PLAY_H

class Play : public Care {
    public:
        Play();
        ~Play();
        void Run();
        void Move();
        void MoveUp();
        void MoveDown();
        void MoveLeft();
        void MoveRight();
        void MoveAdjacentLeftUp();
        void MoveAdjacentRightUP();
        void MoveAdjacentLeftDown();
        void MoveAdjacentRightDown();
};

#endif // PLAY_H
