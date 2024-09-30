// Baby.h


#ifndef BABY_H
#define BABY_H

class Baby : public Care {
    public:
        Baby();
        ~Baby();
        void Run();
        void Eat();
        void Talk();
};

#endif // BABY_H
