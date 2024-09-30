// Birds.h


#ifndef BIRDS_H
#define BIRDS_H

class Birds : public Care {
    public:
        Birds();
        ~Birds();
        void Eat();
        void Run();
        void Fly();
};

#endif // BIRDS_H
