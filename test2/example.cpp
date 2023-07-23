#include <iostream>

#include "sitemasks.h"
#include "sglimits.h"

int main()
{
    PSiteMask sm = SiteBitmask_GR;

    CommMsgBody body;
    sm.compose(body);

    CommMsgParser parser(body);
    PSiteMask m2;
    m2.parse(parser);
    
    isTournLimit(1);

    PString logStr;
    std::cout << "Gr2: " << m2.toDbString(logStr) << ::endl;
}
